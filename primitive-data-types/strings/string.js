////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 1 - INITALIZATION
//
//  Initialize the 'newString' variable as any kind of non-empty string
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let newString = 'This is a new string';

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 2 - TYPE OF
//
//  Get the data type of the 'getMyDataType' variable and save it into
//  the variable 'gotDataType'
let getMyDataType = 'This is a string';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let gotDataType = typeof getMyDataType;

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 3 - STRING LENGTH
//
//  Determine the length of the following variable 'getMyLenght', and save
//  into the variable 'myLength'
let getMyLenght = 'Get the length of this string';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let myLength = getMyLenght.length;

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 4 - STRING CONCATENATION
//
//  Concatenate variables 'concat1', 'concat2', and 'concat3' together
//  and save the result into 'concatStrings'
//  NOTE: You can concatenate with + or with an in-built function
let concat1 = 'No Luke, ';
let concat2 = 'I am your ';
let concat3 = 'father!';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let concatStrings = concat1 + concat2 + concat3;

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 5 - STRING CONTAINS
//
//  Check if variable 'mainString' contains the 'subString' string
//  and save the result into 'stringContains'
//  NOTE: stringContains should be a boolean value of True or False
let mainString = 'Friends are made throughout the day';
let subString = 'out';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let stringContains = mainString.includes('out');

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 6 - STRING CONTAINS IGNORE CASE
//
//  Check if variable 'mainStringIgnoreCase' contains the 'subStringIgnoreCase'
//  string ignoring case, and save the result into 'stringContainsIgnoreCase'
//  NOTE: stringContainsIgnoreCase should be a boolean value of True or False
let mainStringIgnoreCase = 'Friends are made throughout the day';
let subStringIgnoreCase = 'friends';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let stringContainsIgnoreCase = mainStringIgnoreCase
  .toLowerCase()
  .includes(subStringIgnoreCase.toLowerCase());

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 7 - STRING FIRST CHARACTER
//
//  Get the first character of 'getFirstCharacter' and save the result
//  into 'firstCharacter'
let getFirstCharacter = 'You need my first character';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let firstCharacter = getFirstCharacter.charAt(0);

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 8 - STRING FIRST FOUR CHARACTERS
//
//  Get the first four character of 'getFirstFourCharacters' and save the result
//  into 'firstFourCharacters'
let getFirstFourCharacters = 'You need my first four characters';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let firstFourCharacters = getFirstFourCharacters.slice(0, 4);

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 9 - STRING LAST CHARACTER
//
//  Get the last character of 'getLastCharacter' and save the result
//  into 'lastCharacter'
let getLastCharacter = 'You need my last character';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let lastCharacter = getLastCharacter.slice(-1);

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 10 - STRING LAST SIX CHARACTERS
//
//  Get the last six character of 'getLastSixCharacters' and save the result
//  into 'lastSixCharacters'
let getLastSixCharacters = 'You need my last six characters';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let lastSixCharacters = getLastSixCharacters.slice(-6);

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 11 - STRING EQUALS
//
//  Determine if strings 'checkEquality1' and 'checkEquality2' are equal
//  and save the result into 'stringsAreEqual'
let checkEquality1 = 'Are we equal?';
let checkEquality2 = 'Are we equal?';
//  NOTE: 'stringsAreEqual' should be a boolean value of True or False
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let stringsAreEqual = checkEquality1 === checkEquality2;

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 12 - STRING EQUALS IGNORE CASE
//
//  Determine if strings 'checkEqualityIgnoreCase1' and 'checkEqualityIgnoreCase2'
//  are equal, ignoring case, and save the result into 'stringsAreEqualIgnoreCase'
let checkEqualityIgnoreCase1 = 'Are we equal?';
let checkEqualityIgnoreCase2 = 'are we EQUAL?';
//  NOTE: 'stringsAreEqualIgnoreCase' should be a boolean value of True or False
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let stringsAreEqualIgnoreCase =
  checkEqualityIgnoreCase1.toLowerCase() ===
  checkEqualityIgnoreCase2.toLowerCase();

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 13 - STRING REPLACE
//
//  Replace all occurences of "John" with "Michael" in 'replaceMe' and save
//  the result into 'replacedString'
let replaceMe =
  'John just moved to Montreal. John will be meeting his roomate soon.';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let replacedString = replaceMe.replaceAll('John', 'Michael');

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 14 - STRING REMOVE
//
//  Remove 'going to' from the string 'removeMe' so that is makes sense
//  and save the result into removedString
//  Note: You can use the replace function to do so
let removeMe = 'We will going to be leaving at noon sharp.';
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let removedString = removeMe.replace('going to ', '');

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 15 - MULTIPLE MANIPULATIONS 1
//
//  Turn 'testString1':
let testString1 = 'The quick brown fox jumps over the lazy dog';
//  into 'targetString1':
let targetString1 = 'THE-QUICK-BROWN-FOX-JUMPS-OVER-THE-LAZY-DOG';
//  NOTE: Only add functions to testString1 and do not create any new variables
//  The tests will check if testString1 is equal to targetString1
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////
testString1 = testString1.toUpperCase().replaceAll(' ', '-');

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 16 - MULTIPLE MANIPULATIONS 2
//
//  Turn 'testString2':
let testString2 = 'I am the first sentence. You are the second sentence';
//  into 'targetString2':
let targetString2 = 'i am the second best, you are the first best!';
//  Only add functions to testString2 and do not create any new variables
//  The tests will check if testString2 is equal to targetString2
//  Hint: There is more than one way to solve this - be creative!
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

testString2 = testString2
  .toLowerCase()
  .replace('first sentence', 'second best')
  .replace('. you are the second sentence', ', you are the first best!');

////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
//
//  EXERCISE 17 - STRING ESCAPED CHARACTER
//
//  Since strings start and end in quotes, you can't just add a quote
//  midstring as this would signify the end of the string. However, in
//  strings you can add the backwards slash e.g. \" before a character to invoke
//  an alternative interpretation of the character. This is called
//  ESCAPING and is used often by programmers
let escapedString;
//   Uncomment the expression below to see the outcome of the printed variable
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

escapedString =
  'My professor said: "Study hard and you will succeed" \nI replied: "Thanks for the tip!"';

////////////////////////////////////////////////////////////////////////

/////////////////////// END OF STRINGS EXERCISES ///////////////////////

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
if (newString !== undefined && newString.length > 0) {
  console.log(
    correctMsg + "The initialized 'newString' string says '" + newString + "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The initialized 'newString' should be defined and have a length of more than 0, but yours is '" +
      newString +
      "'",
  );
}
totalTests++;

// String Type Of
let correctGotDataType = typeof getMyDataType;
if (gotDataType !== undefined && gotDataType === correctGotDataType) {
  console.log(
    correctMsg +
      "The data type saved into 'gotDataType' you got was '" +
      gotDataType +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The value of the 'gotDataType' variable should be '" +
      correctGotDataType +
      "' but you got '" +
      gotDataType +
      "'",
  );
}
totalTests++;

// String Length
let correctLength = getMyLenght.length;
if (myLength !== undefined && myLength === correctLength) {
  console.log(
    correctMsg +
      "The length of the 'getMyLenght' variable you got was: " +
      myLength,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The length of the 'getMyLenght' variable should be " +
      correctLength +
      ' but you got ' +
      myLength,
  );
}
totalTests++;

// String Concatenation
let correctConcat = concat1.concat(concat2, concat3);
if (concatStrings !== undefined && concatStrings === correctConcat) {
  console.log(
    correctMsg +
      "The value of 'concatStrings' you got was: '" +
      concatStrings +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The value of the 'concatStrings' variable should be '" +
      correctConcat +
      "' but you got '" +
      concatStrings +
      "'",
  );
}
totalTests++;

// String Contains
let correctContains = mainString.includes(subString);
if (stringContains !== undefined && stringContains === correctContains) {
  console.log(
    correctMsg + "The value of 'stringContains' you got was: " + stringContains,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The value of the 'stringContains' variable should be " +
      correctContains +
      ' but you got ' +
      stringContains,
  );
}
totalTests++;

// String Contains Ignore Case
let correctContainsIgnoreCase = mainStringIgnoreCase
  .toLowerCase()
  .includes(subStringIgnoreCase.toLowerCase());
if (
  stringContainsIgnoreCase !== undefined &&
  stringContainsIgnoreCase === correctContainsIgnoreCase
) {
  console.log(
    correctMsg +
      "The value of 'stringContainsIgnoreCase' you got was: " +
      stringContainsIgnoreCase,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The value of the 'stringContainsIgnoreCase' variable should be " +
      correctContainsIgnoreCase +
      ' but you got ' +
      stringContainsIgnoreCase,
  );
}
totalTests++;

// String First Character
let correctFirstCharacter = getFirstCharacter.charAt(0);
if (firstCharacter !== undefined && firstCharacter === correctFirstCharacter) {
  console.log(
    correctMsg +
      "The first character of 'getFirstCharacter' you got was: '" +
      firstCharacter +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The first character of 'getFirstCharacter' should be '" +
      correctFirstCharacter +
      "' but you got '" +
      firstCharacter +
      "'",
  );
}
totalTests++;

// String First Four Characters
let correctFirstFourCharacters = getFirstFourCharacters.substring(0, 4);
if (
  firstFourCharacters !== undefined &&
  firstFourCharacters === correctFirstFourCharacters
) {
  console.log(
    correctMsg +
      "The first four characters of 'getFirstFourCharacter' you got was: '" +
      firstFourCharacters +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The first four characters of 'getFirstFourCharacter' should be '" +
      correctFirstFourCharacters +
      "' but you got '" +
      firstFourCharacters +
      "'",
  );
}
totalTests++;

// String Last Character
let correctLastCharacter = getLastCharacter.charAt(getLastCharacter.length - 1);
if (lastCharacter !== undefined && lastCharacter === correctLastCharacter) {
  console.log(
    correctMsg +
      "The last character of 'getLastCharacter' you got was: '" +
      lastCharacter +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The last character of 'getLastCharacter' should be '" +
      correctLastCharacter +
      "' but you got '" +
      lastCharacter +
      "'",
  );
}
totalTests++;

// String Last Six Characters
let correctLastSixCharacters = getLastSixCharacters.substring(
  getLastSixCharacters.length - 6,
);
if (
  lastSixCharacters !== undefined &&
  lastSixCharacters === correctLastSixCharacters
) {
  console.log(
    correctMsg +
      "The last six characters of 'getLastSixCharacters' you got was: '" +
      lastSixCharacters +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The last six characters of 'getLastSixCharacters' should be '" +
      correctLastSixCharacters +
      "' but you got '" +
      lastSixCharacters +
      "'",
  );
}
totalTests++;

// String Equals
let correctStringEquals = checkEquality1 === checkEquality2;
if (stringsAreEqual !== undefined && stringsAreEqual === correctStringEquals) {
  console.log(
    correctMsg +
      "As for strings 'checkEquality1' and 'checkEquality1' being equal, you said this was: " +
      stringsAreEqual,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "As for strings 'checkEquality1' and 'checkEquality1' being equal, this should be " +
      correctStringEquals +
      ' but you got ' +
      stringsAreEqual,
  );
}
totalTests++;

// String Equals Ignore Case
let correctStringEqualsIgnoreCase =
  checkEqualityIgnoreCase1.toLowerCase() ===
  checkEqualityIgnoreCase2.toLowerCase();
if (
  stringsAreEqualIgnoreCase !== undefined &&
  stringsAreEqualIgnoreCase === correctStringEqualsIgnoreCase
) {
  console.log(
    correctMsg +
      "As for strings 'checkEqualityIgnoreCase1' and 'checkEqualityIgnoreCase2' being equal ignoring case, you said this was: " +
      stringsAreEqualIgnoreCase,
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "As for strings 'checkEqualityIgnoreCase1' and 'checkEqualityIgnoreCase2' being equal ignoring case, this should be " +
      correctStringEqualsIgnoreCase +
      ' but you got ' +
      stringsAreEqualIgnoreCase,
  );
}
totalTests++;

// String Replace
let correctReplace = replaceMe.replace(/John/g, 'Michael');
if (replacedString !== undefined && replacedString === correctReplace) {
  console.log(
    correctMsg +
      "After replacing John with Michael, your 'replacedString' looks like: '" +
      replacedString +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "After replacing John with Michael, your 'replacedString' should be '" +
      correctReplace +
      "' but you got '" +
      replacedString +
      "'",
  );
}
totalTests++;

// String Remove
let correctRemove = removeMe.replace('going to ', '');
if (removedString !== undefined && removedString === correctRemove) {
  console.log(
    correctMsg +
      "After removing \"going to\" from 'removeMe' your 'removedString' looks like: '" +
      removedString +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "After removing \"going to\" from 'removeMe' your 'removedString' should be '" +
      correctRemove +
      "' but you got '" +
      removedString +
      "'",
  );
}
totalTests++;

// Multiple Manipulations 1
// Since we already have a target string, we don't need to create a correct test variable
if (testString1 === targetString1) {
  console.log(
    correctMsg +
      "After your manipulations to 'testString1', it now looks like: '" +
      testString1 +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "After your manipulations to 'testString1', it should be '" +
      targetString1 +
      "' but you got '" +
      testString1 +
      "'",
  );
}
totalTests++;

// Multiple Manipulations 2
// Since we already have a target string, we don't need to create a correct test variable
if (testString2 === targetString2) {
  console.log(
    correctMsg +
      "After your manipulations to 'testString2', it now looks like: '" +
      targetString2 +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "After your manipulations to 'testString2', it should be '" +
      targetString2 +
      "' but you got '" +
      testString2 +
      "'",
  );
}
totalTests++;

// Escaped String
let correctEscapedString =
  'My professor said: "Study hard and you will succeed" \nI replied: "Thanks for the tip!"';
if (escapedString !== undefined && escapedString === correctEscapedString) {
  console.log(
    correctMsg +
      "The 'escapedString' with escaped quotes looks like: \n'" +
      escapedString +
      "'",
  );
  passedTests++;
} else {
  console.log(
    incorrectMsg +
      "The 'escapedString' with escaped quotes should be:\n'" +
      correctEscapedString +
      "'\n but you got '" +
      escapedString +
      "'",
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
