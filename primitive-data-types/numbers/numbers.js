////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 1 - INITALIZATION
//
//  Initialize the 'newNumber' variable as any kind of number
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let newNumber = 10.223;

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 2 - IS NUMBER
//
//  Check if variables 'isNumer1' and 'isNumber2' are numbers and save
//  the result into 'number1IsNumber' and 'number2IsNumber' respectively
let isNumber1 = 'Nan';
let isNumber2 = 4000;
//  NOTE: 'number1IsNumber' and 'number2IsNumber' should be boolean values
//  of True or False. The code will indeed be the same for both variables
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let number1IsNumber = typeof isNumber1 === 'number';
let number2IsNumber = typeof isNumber2 === 'number';

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 3 - ABSOLUTE VALUE
//
//  Get the absolute value of 'getMyAbsoluteValue' and save the result
//  into 'absoluteValue'
let getMyAbsoluteValue = -99;
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let absoluteValue = Math.abs(getMyAbsoluteValue);

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 4 - ROUND UP A NUMBER
//
//  Round up the variable 'roundMeUp' to the nearest integer and save the
//  the result into 'roundedUpNumber'
let roundMeUp = 85.4;
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let roundedUpNumber = Math.ceil(roundMeUp);

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 5 - ROUND DOWN A NUMBER
//
//  Round down the variable 'roundMeDown' to the nearest integer and save the
//  the result into 'roundedDownNumber'
let roundMeDown = 85.4;
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let roundedDownNumber = Math.floor(roundMeDown);

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 6 - NUMBER TO THE POWER
//
//  Calculate 'baseNumber' to the power of 'powerNumber' and save the
//  result into 'baseToThePower'
let baseNumber = 2;
let powerNumber = 9;
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let baseToThePower = baseNumber ** powerNumber;

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 7 - PERCENTAGE CALCULATION TO 2 DECIMAL PLACES
//
//  Calculate the percentage of 'scoreValue' out of 'maxValue' to
//  2 decimal places and save the result into 'scorePercentage'
let scoreValue = 67;
let maxValue = 145;
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let scorePercentage = ((scoreValue / maxValue) * 100).toFixed(2);

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 8 - Add number to string
//
//  Add the number in variable 'score' to the end of the string variable
//  'messagePrefix' and save it into the variable 'scoreMessage'
let messagePrefix = 'You got a score of';
let score = 145;
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let scoreMessage = messagePrefix + ' ' + score;

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 9 - Parse float from string
//
//  Parse the number from string variable 'parseTheNumber' and save it into
//  'parsedNumber' which should be of number data type
let parseTheNumber = 'You got a score of 25.5';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let parsedNumber = parseFloat(parseTheNumber.match(/\d+(\.\d+)?/)[0]);

////////////////////////////////////////////////////////////////////////

/////////////////////// END OF NUMBERS EXERCISES ///////////////////////

////////////////////////////////////////////////////////////////////////
//
//                               ANSWERS
//
//  DO NOT LOOK AT THIS SECTION UNTIL YOU HAVE FINISHED THE EXERCISES
//
//  The following code tests the variables you need to work on to confirm your work is
//  correct. The if conditions check the variables are correct and the console.log()
//  statements are what make the print outs you see when you run the file. The below
//  is a crude demonstration of what we refer to as code tests. Code testing is a
//  common practice in the software engineer's role, where tests are run to confirm all
//  code runs correctly. Only when all tests pass would we give ourselves the green light
//  to ship code to production and feel confident the system will perform as expected.
//
////////////////////////////////////////////////////////////////////////

// setGreen instructs the shell to set the printed output to green
let setGreen = '\x1b[32m';
// setRed instructs the shell to set the printed output to red
let setRed = '\x1b[31m';
// resetColor instructs the shell to reset the printout color to standard
let resetColor = '\x1b[0m';

// Set correctMsg and incorrectMsg Messages so I don't need to write it everytimne
let correctMsg = setGreen + 'Correct! ' + resetColor;
let incorrectMsg = setRed + 'Incorrect! ' + resetColor;

// totalTests and passedTests count the final tally of passed tests
let totalTests = 0;
let passedTests = 0;

// Number Initialization
if (newNumber !== undefined && typeof newNumber === 'number') {
  console.log(
    correctMsg +
      "You initialized the 'newNumber' number variable as " +
      newNumber,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The initialized 'newNumber' should be defined and be a number, but yours is " +
      newNumber,
  );
}
totalTests++;

// Variable Is Number 1
let correctNumber1IsNumber = typeof isNumber1 === 'number';
if (
  number1IsNumber !== undefined &&
  number1IsNumber == correctNumber1IsNumber
) {
  console.log(
    correctMsg +
      "As for the variable 'isNumber1' being a number, you found this was " +
      number1IsNumber,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "As for the variable 'isNumber1' being a number, this should be " +
      correctNumber1IsNumber +
      ' but you got ' +
      number1IsNumber,
  );
}
totalTests++;

// Variable Is Number 2
let correctNumber2IsNumber = typeof isNumber2 === 'number';
if (
  number2IsNumber !== undefined &&
  number2IsNumber == correctNumber2IsNumber
) {
  console.log(
    correctMsg +
      "As for the variable 'isNumber1' being a number, you found this was " +
      number2IsNumber,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "As for the variable 'isNumber2' being a number, this should be " +
      correctNumber2IsNumber +
      ' but you got ' +
      number2IsNumber,
  );
}
totalTests++;

// Absolute Value
let correctAbsoluteValue = Math.abs(getMyAbsoluteValue);
if (absoluteValue !== undefined && absoluteValue == correctAbsoluteValue) {
  console.log(
    correctMsg +
      "The absolute value of 'getMyAbsoluteValue' you got was " +
      absoluteValue,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The absolute value of 'getMyAbsoluteValue' should be " +
      correctAbsoluteValue +
      ' but you got ' +
      absoluteValue,
  );
}
totalTests++;

// Round Up A Number
let correctRoundedUpNumber = Math.ceil(roundMeUp);
if (
  roundedUpNumber !== undefined &&
  roundedUpNumber === correctRoundedUpNumber
) {
  console.log(
    correctMsg +
      "The rounded up value of 'roundMeUp' you got was " +
      roundedUpNumber,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The rounded up value of 'roundMeUp' should be " +
      correctRoundedUpNumber +
      ' but you got ' +
      roundedUpNumber,
  );
}
totalTests++;

// Round Down A Number
let correctRoundedDownNumber = Math.floor(roundMeDown);
if (
  roundedDownNumber !== undefined &&
  roundedDownNumber === correctRoundedDownNumber
) {
  console.log(
    correctMsg +
      "The rounded down value of 'roundMeDown' you got was " +
      roundedDownNumber,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The rounded down value of 'roundMeDown' should be " +
      correctRoundedDownNumber +
      ' but you got ' +
      roundedDownNumber,
  );
}
totalTests++;

// Number to the power
let correctBaseToThePower = baseNumber ** powerNumber;
if (baseToThePower !== undefined && baseToThePower === correctBaseToThePower) {
  console.log(
    correctMsg +
      "The 'baseNumber' to the power of 'powerNumber' you got was " +
      baseToThePower,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The 'baseNumber' to the power of 'powerNumber' should be " +
      correctBaseToThePower +
      ' but you got ' +
      baseToThePower,
  );
}
totalTests++;

// Percentage Calculation To 2 Decimal Places
let correctScorePercentage = ((scoreValue / maxValue) * 100).toFixed(2);
if (
  scorePercentage !== undefined &&
  scorePercentage === correctScorePercentage
) {
  console.log(
    correctMsg +
      "The percentage of 'scoreValue' out of 'maxValue' to 2 decimal places you got was " +
      scorePercentage,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The percentage of 'scoreValue' out of 'maxValue' to 2 decimal places should be " +
      correctScorePercentage +
      ' but you got ' +
      scorePercentage,
  );
}
totalTests++;

// Add number to string
let correctScoreMessage = messagePrefix + ' ' + score;
if (scoreMessage !== undefined && scoreMessage === correctScoreMessage) {
  console.log(
    correctMsg + "The vale of 'scoreMessage' you got was " + scoreMessage,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The vale of 'scoreMessage' should be '" +
      correctScoreMessage +
      "' but you got " +
      scoreMessage,
  );
}
totalTests++;

// Parse number from string
let correctParsedNumber = parseFloat(parseTheNumber.replace(/[^0-9.]/g, ''));
if (parsedNumber !== undefined && parsedNumber === correctParsedNumber) {
  console.log(
    correctMsg +
      "The vale of 'parsedNumber' you got was " +
      parsedNumber +
      ' of type ' +
      typeof parsedNumber,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The vale of 'parsedNumber' should be " +
      correctParsedNumber +
      ' of type ' +
      typeof correctParsedNumber +
      ' but you got ' +
      parsedNumber +
      ' of type ' +
      typeof parsedNumber,
  );
}
totalTests++;

// Final Test Tally Determination
if (passedTests === totalTests) {
  console.log(
    setGreen +
      'You passed ' +
      passedTests +
      ' / ' +
      totalTests +
      ' tests. Congratulations!' +
      resetColor,
  );
} else {
  console.log(
    setRed +
      'You passed ' +
      passedTests +
      ' / ' +
      totalTests +
      ' tests. Keep Going!' +
      resetColor,
  );
}
