//Global Variables
let username = '';
let startUpAmount = 1000;
let numberOfRounds = 0;
//HTML IDS
const userNameId = 'craps-input';
const registrationPane = 'registration-pane';
const mainGameStats = 'main-game-stats';
const mainGame = 'main-game';
const user = 'user';
const round = 'rounds';
const amount = 'amount';
const roundManager = 'round-manager';

//In Game Variables
currentRounds = numberOfRounds;
currentAmount = startUpAmount;

function getCrapPlayerUsername() {
  username = document.getElementById(userNameId).value;
  console.log(username);

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
  startUpMoney(currentAmount);
  gameRounds(currentRounds);
}

function startUpMoney(money) {
  document.getElementById(amount).innerHTML = money;
}

function gameRounds(number) {
  document.getElementById(round).innerHTML = number;
}
