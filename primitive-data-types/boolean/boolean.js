////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 1 - INITALIZATION
//
//  Initialize the 'newBoolean' variable as a boolean literal of value true
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let newBoolean = 'True';

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 2 - MOM VS DAD HEIGHT
//
//  We generate mom and dad's height randomly, use comparison operators to:
//  - Check if 'momsHeight' was greater than 'dadsHeight', saved into 'momIsTaller'
//  - Check if 'dadsHeight' was greater than 'momsHeight', saved into 'dadIsTaller'
//  - Check if 'dadsHeight' equals 'momsHeight', saved into 'areTheSameHeight'
let momsHeight = generateRandomNumber(100, 200);
let dadsHeight = generateRandomNumber(100, 200);
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let momIsTaller = momsHeight > dadsHeight;
let dadIsTaller = dadsHeight > momsHeight;
let areTheSameHeight = dadsHeight === momsHeight;

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 3 - NOT PLAGIARISM?
//
//  As the teacher you are grading student's book reports. You heard through
//  the grapevine students found a website online to copy from, and found a key
//  phrase you think many students would use. TO ensure they did not, check
//  if 'studentEssay' DO NOT contain the substring 'keyPhrase'.
let keyPhrase = 'demonstrates his nostalgic tendencies';
let studentEssay = generateSudentEssay();
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let notPlagiarised = !studentEssay.includes(keyPhrase);

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 4 - SIBLINGS HEIGHT
//
//  We generate sister's and brother's height randomly, use logical operators to:
//  - Check if BOTH 'sistersHeight' and 'brothersHeight are above the 'thresholdForTall', saved into 'siblingsAreTall'
//  - Check if BOTH 'sistersHeight' and 'brothersHeight are below the 'thresholdForTall', saved into 'siblingsAreShort'
//  - Check if AT LEAST ONE of them are taller than 'thresholdForTall', saved into 'atLeastOneIsTall'
//  - Check if only one of 'sistersHeight' or 'brothersHeight are above the 'thresholdForTall'
//    BUT NOT BOTH, saved into 'onlyOneIsTall'
let sistersHeight = generateRandomNumber(100, 200);
let brothersHeight = generateRandomNumber(100, 200);
let thresholdForTall = 150;
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let siblingsAreTall =
  sistersHeight > thresholdForTall && brothersHeight > thresholdForTall;
let siblingsAreShort =
  sistersHeight < thresholdForTall && brothersHeight < thresholdForTall;
let atLeastOneIsTall =
  sistersHeight > thresholdForTall || brothersHeight > thresholdForTall;
let onlyOneIsTall =
  (sistersHeight > thresholdForTall && brothersHeight <= thresholdForTall) ||
  (brothersHeight > thresholdForTall && sistersHeight <= thresholdForTall);

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 5 - VALIDATE A SECRET CODE
//
//  Your friend in class sends you a note with a secret code, you need to
//  validate this 'secretCode', the validation rules are as follows:
//  - The 5th character must be an upper case letter
//  - The 10th character must be a digit
//  - The code must be 15 characters long
//  All of these conditions must be met for the code to be validated, save
//  the result into 'codeIsValid'
let secretCode = generateSecretCode();
//  Hint: This boolean expression is somewhat complicated, you could create
//  numerous variables for each check, and combine them at the end
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let fifthIsUppercase = secretCode[4] >= 'A' && secretCode[4] <= 'Z';
let tenthIsDigit = secretCode[9] >= '0' && secretCode[9] <= '9';
let correctLength = secretCode.length === 15;
let codeIsValid = fifthIsUppercase && tenthIsDigit && correctLength;

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 6 - TRUTHY AND FALSY
//
//  As well as a type, each value also has an inherent boolean value,
//  generally known as either truthy or falsy. Some of the rules are a
//  little bizarre so have a look at the following conversions using
//  the Boolean() conversion function, which will look at the non-boolean
//  data types and return their inherent boolean value
let falsy1, falsy2, falsy3, falsy4, falsy5;
let truthy1, truthy2;
//  Uncomment the lines below to see what they evaluate to
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

falsy1 = Boolean('');
falsy2 = Boolean(0);
falsy3 = Boolean(undefined);
falsy4 = Boolean(null);

truthy1 = Boolean('non-empty string');
truthy2 = Boolean(1);

////////////////////////////////////////////////////////////////////////

/////////////////////// END OF BOOLEANS EXERCISES //////////////////////

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

// String Initialization
if (newBoolean !== undefined && newBoolean) {
  console.log(
    correctMsg + "The initialized 'newBoolean' is '" + newBoolean + "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The initialized 'newBoolean' should be defined and be 'true', but yours is '" +
      newBoolean +
      "'",
  );
}
totalTests++;

// Mom vs Dad height
let correctMomIsTaller = momsHeight > dadsHeight;
let correctDadIsTaller = dadsHeight > momsHeight;
let correctSameHeight = momsHeight === dadsHeight;
if (
  momIsTaller !== undefined &&
  momIsTaller === correctMomIsTaller &&
  dadIsTaller !== undefined &&
  dadIsTaller === correctDadIsTaller &&
  areTheSameHeight !== undefined &&
  areTheSameHeight === correctSameHeight
) {
  console.log(correctMsg + 'Passed Mom vs data height:');
  console.log(
    "\tMom's height was " +
      momsHeight +
      "cm and dad's height was " +
      dadsHeight +
      'cm',
  );
  console.log("\tValue of 'momIsTaller' you got was '" + momIsTaller + "'");
  console.log("\tValue of 'dadIsTaller' you got was '" + dadIsTaller + "'");
  console.log(
    "\tValue of 'areTheSameHeight' you got was'" + areTheSameHeight + "'",
  );
  passedTests++;
} else {
  console.log(incorrectMsg + 'Failed Mom vs data height:');
  console.log(
    "\tMom's height was " +
      momsHeight +
      "cm and dad's height was " +
      dadsHeight +
      'cm',
  );
  console.log(
    "\t'momIsTaller' should be '" +
      correctMomIsTaller +
      "' and you got '" +
      momIsTaller +
      "'",
  );
  console.log(
    "\t'dadIsTaller' should be '" +
      correctDadIsTaller +
      "' and you got '" +
      dadIsTaller +
      "'",
  );
  console.log(
    "\t'areTheSameHeight' should be '" +
      correctSameHeight +
      "' and you got '" +
      areTheSameHeight +
      "'",
  );
}
totalTests++;

// Not plagiarism
let correctNotPlagiarised = !studentEssay.includes(keyPhrase);
if (notPlagiarised !== undefined && notPlagiarised === correctNotPlagiarised) {
  console.log(
    correctMsg +
      "The value of 'notPlagiarised' you got was '" +
      notPlagiarised +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The value of 'notPlagiarised' should be '" +
      correctNotPlagiarised +
      "' but you got '" +
      notPlagiarised +
      "'",
  );
}
totalTests++;

// Siblings height
let correctAllAreTall =
  sistersHeight >= thresholdForTall && brothersHeight >= thresholdForTall;
let correctAllAreShort =
  sistersHeight < thresholdForTall && brothersHeight < thresholdForTall;
let correctAtLeastOneIsTall =
  sistersHeight >= thresholdForTall || brothersHeight >= thresholdForTall;
let correctOnlyOneIsTall =
  (sistersHeight > thresholdForTall && brothersHeight < thresholdForTall) ||
  (sistersHeight < thresholdForTall && brothersHeight > thresholdForTall);

if (
  siblingsAreTall !== undefined &&
  siblingsAreTall === correctAllAreTall &&
  siblingsAreShort !== undefined &&
  siblingsAreShort === correctAllAreShort &&
  atLeastOneIsTall !== undefined &&
  atLeastOneIsTall === correctAtLeastOneIsTall &&
  onlyOneIsTall !== undefined &&
  onlyOneIsTall === correctOnlyOneIsTall
) {
  console.log(correctMsg + 'Passed siblings height:');
  console.log(
    "\tSister's height was " +
      sistersHeight +
      "cm and brother's height was " +
      brothersHeight +
      'cm, threshold was ' +
      thresholdForTall +
      'cm.',
  );
  console.log(
    "\tValue of 'siblingsAreTall' you got was '" + siblingsAreTall + "'",
  );
  console.log(
    "\tValue of 'siblingsAreShort' you got was '" + siblingsAreShort + "'",
  );
  console.log(
    "\tValue of 'atLeastOneIsTall' you got was'" + atLeastOneIsTall + "'",
  );
  console.log("\tValue of 'onlyOneIsTall' you got was'" + onlyOneIsTall + "'");
  passedTests++;
} else {
  console.log(incorrectMsg + 'Failed siblings height:');
  console.log(
    "\tSister's height was " +
      sistersHeight +
      "cm and brother's height was " +
      brothersHeight +
      'cm, threshold was ' +
      thresholdForTall +
      'cm.',
  );
  console.log(
    "\t'siblingsAreTall' should be '" +
      correctAllAreTall +
      "' and you got '" +
      siblingsAreTall +
      "'",
  );
  console.log(
    "\t'siblingsAreShort' should be '" +
      correctAllAreShort +
      "' and you got '" +
      siblingsAreShort +
      "'",
  );
  console.log(
    "\t'atLeastOneIsTall' should be '" +
      correctAtLeastOneIsTall +
      "' and you got '" +
      atLeastOneIsTall +
      "'",
  );
  console.log(
    "\t'onlyOneIsTall' should be '" +
      correctOnlyOneIsTall +
      "' and you got '" +
      onlyOneIsTall +
      "'",
  );
}
totalTests++;

// Validating a secret code
let correctCodeIsValid =
  secretCode.charCodeAt(4) >= 65 &&
  secretCode.charCodeAt(4) <= 90 &&
  secretCode.charCodeAt(9) >= 48 &&
  secretCode.charCodeAt(9) <= 57 &&
  secretCode.length === 15;
if (codeIsValid !== undefined && codeIsValid === correctCodeIsValid) {
  console.log(
    correctMsg +
      "The code was '" +
      secretCode +
      "' so value of 'codeIsValid' you got was '" +
      codeIsValid +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The code was '" +
      secretCode +
      "' so the value of 'codeIsValid' should be '" +
      correctCodeIsValid +
      "' but you got '" +
      codeIsValid +
      "'",
  );
}
totalTests++;

// Truthy vs Falsy
if (
  falsy1 !== undefined &&
  !falsy1 &&
  falsy2 !== undefined &&
  !falsy2 &&
  falsy3 !== undefined &&
  !falsy3 &&
  falsy4 !== undefined &&
  !falsy4 &&
  truthy1 !== undefined &&
  truthy1 &&
  truthy2 !== undefined &&
  truthy2
) {
  console.log(correctMsg + 'Passed falsy and truthy values:');
  console.log('\tFalsy values:');
  console.log(
    '\tThe expression [ Boolean("") ]          evaluates to ' + falsy1,
  );
  console.log(
    '\tThe expression [ Boolean(0) ]           evaluates to ' + falsy2,
  );
  console.log(
    '\tThe expression [ Boolean(undefined) ]   evaluates to ' + falsy3,
  );
  console.log(
    '\tThe expression [ Boolean(null) ]        evaluates to ' + falsy4,
  );
  console.log('\tTruthy values:');
  console.log(
    '\tThe expression [ Boolean("non-empty") ] evaluates to ' + truthy1,
  );
  console.log(
    '\tThe expression [ Boolean(1) ]           evaluates to ' + truthy2,
  );
  passedTests++;
} else {
  console.log(incorrectMsg + 'Failed falsy and truthy values:');
  console.log('\tFalsy values:');
  console.log(
    '\tThe expression [ Boolean("") ] should be saved into \'falsy1\'',
  );
  console.log("\tThe expression [ Boolean(0) ] should be saved into 'falsy2'");
  console.log(
    "\tThe expression [ Boolean(undefined) ] should be saved into 'falsy3'",
  );
  console.log(
    "\tThe expression [ Boolean(null) ] should be saved into 'falsy4'",
  );
  console.log('\tTruthy values:');
  console.log(
    '\tThe expression [ Boolean("non-empty") ] should be saved into \'truthy1\'',
  );
  console.log("\tThe expression [ Boolean(1) ] should be saved into 'truthy2'");
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

//////////////////////////// END OF ANSWERS ////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//                           HELPER FUNCTIONS
//
//  FEEL FREE TO LOOK AT THIS SECTION
//
//  The following code generates some variables that you need to check.
//  So you do not cheat, they generate them on a random basis that you
//  cannot predict. So you cannot and must perform the exercises the
//  right way. You can look at them though, they leverage conditionals
//  (if - else) to generate the values used in the tests, and we will
//  see conditionals in the 'Control Flows' chapter of this course
//
////////////////////////////////////////////////////////////////////////

// generateRandomNumber returns a random number between min and max (included)
// so that you cannot cheat and write boolean literals based on the exercise setup
function generateRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// generateSudentEssay returns one of two versions of an assay randomly, so that
// you cannot cheat and write boolean literals based on the exercise setup
function generateSudentEssay() {
  if (generateRandomNumber(0, 10) < 5) {
    return 'The expression on his face as he looked at the retro artwork demonstrates his nostalgic tendencies, especially for the times when technology was begining to pervade society.';
  }
  return 'The fact the retro artwork made him smile showed his deep longing for the past, especially for the time when technology began to pervade society and the outlook was still positive.';
}

// generateSecretCode returns a secret code that sometimes passes validation, sometimes
// doesn't, so that you cannot cheat and write boolean literals based on the exercise setup
function generateSecretCode() {
  let code = 'aj9s';
  // Add characters 5 - 9
  if (generateRandomNumber(0, 10) < 7) {
    code += 'Basdd';
  } else {
    code += 'bmki9';
  }
  // Add characters 9 - 14
  if (generateRandomNumber(0, 10) < 7) {
    code += '58yhs';
  } else {
    code += 'bKols';
  }
  // Add trailing characters
  if (generateRandomNumber(0, 10) < 7) {
    code += '5';
  } else {
    // Make it more than 15 characters
    code += 'asd0';
  }
  return code;
}
