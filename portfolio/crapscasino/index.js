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
let currentMoney = startUpAmount - userBetAmount;
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
  betChoices.forEach((id) => {
    document.getElementById(id).style.backgroundColor = '';
  });
  document.getElementById(move).style.backgroundColor = 'red';
  currentBet = move;
  console.log(currentBet);
}
function increaseBet() {
  const next = Math.min(
    userBetAmount + minimumBet,
    currentMoney + userBetAmount,
  );
  const delta = next - userBetAmount;
  userBetAmount = next;
  currentMoney -= delta;
  SetBetAmount();
}
function decreaseBet() {
  const next = Math.max(userBetAmount - minimumBet, minimumBet);
  const delta = userBetAmount - next;
  userBetAmount = next;
  currentMoney += delta;
  SetBetAmount();
}
function SetBetAmount() {
  document.getElementById(userBetId).innerHTML = userBetAmount;
  resetCurentMoney();
}
function resetCurentMoney() {
  document.getElementById(amount).innerHTML = currentMoney;
}
