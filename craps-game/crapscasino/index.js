//Global Variables
let username = '';

//HTML IDS
const userNameId = 'craps-input';
const registrationPane = 'registration-pane';
const mainGameStats = 'main-game-stats';
const mainGame = 'main-game';
const user = 'user';
const round = 'rounds';
const amount = 'amount';
const roundManager = 'round-manager';
const userBetId = 'user-bet-amount';
let activeBet = 0;

//In built game variables
const bet = {
  even: 'even',
  odd: 'odd',
};
const betChoices = [bet.even, bet.odd];
let startUpAmount = 1000;
let numberOfRounds = 0;
let minimumBet = 100;
let userBetAmount = minimumBet;
let currentBet = undefined;
let currentRounds = numberOfRounds;
let currentMoney = startUpAmount;
let canChooseBet = true;
let delta = 0;
let next = 0;
let win = false;
let haveMadeBet = false;
//currentAmount = startUpAmount;

function getCrapPlayerUsername() {
  username = document.getElementById(userNameId).value;

  let validRegexChars = /^[0-9]|[^a-zA-Z0-9_]/g;
  if (username.length < 5 || validRegexChars.test(username)) {
    alert(
      'Username must not have a space and should not begin with a number and should not be less than 5 characters and should only have aphanumeric characters',
    );
  } else {
    removeRegistrationPane();
    showMainGame();
    firstRound();
  }
}

function removeRegistrationPane() {
  document.getElementById(registrationPane).style.display = 'none';
}
function showMainGame() {
  document.getElementById(mainGame).style.display = 'flex';
  document.getElementById(mainGame).style.justifyContent = 'center';
  //document.getElementById(roundManager).style.display = 'flex';
  //document.getElementById(roundManager).style.justifyContent = 'center';
}
function firstRound() {
  document.getElementById(user).innerHTML = username;
  currentRounds = numberOfRounds;
  currentAmount = startUpAmount;
  startUpMoney(currentMoney);
  gameRounds(currentRounds);
  SetBetAmount();
}

function startUpMoney(money) {
  document.getElementById(amount).innerHTML = money;
}

function gameRounds(number) {
  document.getElementById(round).innerHTML = number;
}

function evenSelector() {
  chooseBet(bet.even);
}
function oddSelector() {
  chooseBet(bet.odd);
}
function chooseBet(move) {
  if (canChooseBet) {
    betChoices.forEach((id) => {
      document.getElementById(id).style.backgroundColor = '';
    });
    document.getElementById(move).style.backgroundColor = 'red';
    currentBet = move;
    console.log(currentBet);
    haveMadeBet = true;
  }
}
function increaseBet() {
  if (canChooseBet && userBetAmount < currentMoney) {
    next = Math.min(userBetAmount + minimumBet, currentMoney + userBetAmount);
    userBetAmount = next;
    SetBetAmount();
  }
}
function decreaseBet() {
  if (canChooseBet && userBetAmount > minimumBet) {
    next = Math.max(userBetAmount - minimumBet, minimumBet);
    userBetAmount = next;
    SetBetAmount();
  }
}
function SetBetAmount() {
  document.getElementById(userBetId).innerHTML = userBetAmount;
  //resetCurentMoney();
}
function resetCurentMoney() {
  document.getElementById(amount).innerHTML = currentMoney;
}
function diceRollFunc() {
  if (haveMadeBet) {
    canChooseBet = false;
    activeBet = userBetAmount;
    const diceRoll = document.getElementById('dice-roll-container');
    rollADie({
      element: diceRoll,
      numberOfDice: 2,
      callback: callBackToDiceRoll,
      delay: 1000000,
    });
  } else {
    showToast("You haven't made a bet yet");
  }
}
function resetGame() {
  document.getElementById('reset-end').style.display = 'flex';
}
function callBackToDiceRoll(diceResult) {
  document.getElementById('roll-dice').style.display = 'none';
  const result = diceResult[0] + diceResult[1];
  const rolledEven = result % 2 === 0;
  win =
    (rolledEven && currentBet === 'even') ||
    (!rolledEven && currentBet === 'odd');

  amountRecalculation(result);
  resetGame();
}
function amountRecalculation(result) {
  if (win) {
    currentMoney += activeBet;
    setResult(`You rolled ${result} — you win!`, 'win');
  } else {
    currentMoney -= activeBet;
    setResult(`You rolled ${result} — you loose!`, 'loose');
  }
  resetCurentMoney();
}
function nextRound() {
  if (currentMoney >= minimumBet) {
    currentRounds += 1;
    canChooseBet = true;
    win = false;
    haveMadeBet = false;
    currentBet = undefined;
    userBetAmount = minimumBet;

    // restore the parts of the UI the previous round changed
    document.getElementById('roll-dice').style.display = '';
    document.getElementById('reset-end').style.display = 'none';
    document.getElementById('dice-roll-container').innerHTML = '';
    document.getElementById('result').textContent = '';
    document.getElementById('result').className = '';
    betChoices.forEach((id) => {
      document.getElementById(id).style.backgroundColor = '';
    });

    gameRounds(currentRounds);
    resetCurentMoney();
    SetBetAmount();
  } else {
    showToast('You have run out of cash');
    endGame();
  }
}

function setResult(text, outcome) {
  const result = document.getElementById('result');
  result.textContent = text;
  result.className = '';
  result.classList.add('show', outcome);
}
function endGame() {
  startUpAmount = 1000;
  numberOfRounds = 0;
  minimumBet = 100;
  userBetAmount = minimumBet;
  currentBet = undefined;
  currentRounds = numberOfRounds;
  currentMoney = startUpAmount;
  canChooseBet = true;
  delta = 0;
  next = 0;
  win = false;
  haveMadeBet = false;
  activeBet = 0;
  username = '';

  document.getElementById(userNameId).value = ''; // clear the stale input
  document.getElementById(mainGame).style.display = 'none'; // hide the game
  document.getElementById(registrationPane).style.display = 'flex'; // show the form
  document.getElementById('roll-dice').style.display = '';
  document.getElementById('reset-end').style.display = 'none';
  document.getElementById('dice-roll-container').innerHTML = '';
  document.getElementById('result').textContent = '';
  document.getElementById('result').className = '';
  betChoices.forEach((id) => {
    document.getElementById(id).style.backgroundColor = '';
  });
}
let toastTimeout;
function showToast(message) {
  const toast = document.getElementById('toast');
  clearTimeout(toastTimeout);
  toast.textContent = message;
  toast.classList.add('show');
  toastTimeout = setTimeout(() => {
    toast.classList.remove('show');
  }, 2500);
}
