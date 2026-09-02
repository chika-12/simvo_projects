const settingsForm = document.getElementById('settings-form');
//let toastTimeout;
// function showToast(message) {
//   const toast = document.getElementById('toast');
//   clearTimeout(toastTimeout);
//   toast.textContent = message;
//   toast.classList.add('show');
//   toastTimeout = setTimeout(() => {
//     toast.classList.remove('show');
//   }, 2500);
// }

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

  if (Object.values(gameSettings).some((v) => Number.isNaN(v) || v <= 0)) {
    showToast('Please enter valid positive numbers for all settings');
    return;
  }

  localStorage.setItem('gameSettings', JSON.stringify(gameSettings));

  showToast('Settings Saved');

  //alert('Settings saved!');
});
