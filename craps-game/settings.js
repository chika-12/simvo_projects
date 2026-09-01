const settingsForm = document.getElementById('settings-form');

settingsForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const startUpAmount = Number(
    document.getElementById('start-up-amount').value,
  );

  const minimumBet = Number(document.getElementById('minimum-bet').value);

  const numberOfDice = Number(document.getElementById('number-of-dice').value);

  const delayTime = Number(document.getElementById('delay-time').value);

  const gameSettings = {
    startUpAmount,
    minimumBet,
    numberOfDice,
    delayTime,
  };

  localStorage.setItem('gameSettings', JSON.stringify(gameSettings));

  alert('Settings saved!');
});
