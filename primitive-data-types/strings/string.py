########################################################################
#
#  EXERCISE 1 - INITALIZATION
#
#  Initialize the 'newString' variable as any kind of non-empty string
#
###################### YOUR CODE BELOW THIS LINE #######################

newString = "This is a new string"

########################################################################



########################################################################
#
#  EXERCISE 2 - TYPE OF
#
#  Get the data type of the 'getMyDataType' variable and save it into
#  the variable 'gotDataType'
getMyDataType = "This is a string"
#
###################### YOUR CODE BELOW THIS LINE #######################

gotDataType = type(getMyDataType)

########################################################################



########################################################################
#
#  EXERCISE 3 - STRING LENGTH
#
#  Determine the length of the following variable 'getMyLenght', and save
#  into the variable 'myLength'
getMyLenght = "Get the length of this string"
#  NOTE: This uses one of the only properties that exists for strings
#
###################### YOUR CODE BELOW THIS LINE #######################

myLength = len(getMyLenght)

########################################################################



########################################################################
#
#  EXERCISE 4 - STRING CONCATENATION
#
#  Concatenate variables 'concat1', 'concat2', and 'concat3' together
#  and save the result into 'concatStrings'
#  NOTE: You can concatenate with + or with an in-built function
concat1 = "No Luke, "
concat2 = "I am your "
concat3 = "father!"
#
###################### YOUR CODE BELOW THIS LINE #######################

concatStrings = concat1 + concat2 + concat3

########################################################################



########################################################################
#
#  EXERCISE 5 - STRING REPETITION
#
#  I've generated a random integer between 1 and 5 and saved it into 'repeatTimes'
from random import randrange
repeatTimes = randrange(1, 5)
#  Repeat the string 'repeatMe' a total of 'repeatTimes' using the multiplier operator
#  and save the result into the variable 'repeatedString'. Since 'repeatTimes'
#  is randomly generated, you can't just concatenate 'repeatMe', find another way!
repeatMe = "Let it snow! "
#
###################### YOUR CODE BELOW THIS LINE #######################

repeatedString = repeatMe * repeatTimes

########################################################################



########################################################################
#
#  EXERCISE 6 - STRING CONTAINS
#
#  Check if variable 'mainString' contains the 'subString' string
#  and save the result into 'stringContains'
#  NOTE: stringContains should be a boolean value of True or False
mainString = "Friends are made throughout the day"
subString = "out"
#
###################### YOUR CODE BELOW THIS LINE #######################

stringContains = subString in mainString

########################################################################



########################################################################
#
#  EXERCISE 7 - STRING FIND
#
#  Find the index in 'findSubstring' where string 'subStringToFind' occurs
#  and save the result into 'foundSubstringIndex'
#  NOTE: 'foundSubstringIndex' should be an integer value
findSubstring = "Messi is the best soccer player"
subStringToFind = "best"
#
###################### YOUR CODE BELOW THIS LINE #######################

foundSubstringIndex = findSubstring.find(subStringToFind)

########################################################################



########################################################################
#
#  EXERCISE 8 - STRING FIRST CHARACTER
#
#  Get the first character of 'getFirstCharacter' and save the result
#  into 'firstCharacter'
getFirstCharacter = "You need my first character"
#
###################### YOUR CODE BELOW THIS LINE #######################

firstCharacter = getFirstCharacter[0]

########################################################################



########################################################################
#
#  EXERCISE 9 - STRING FIRST SEVEN CHARACTERS
#
#  Get the first seven character of 'getFirstSevenCharacters' and save the result
#  into 'firstSevenCharacters'
getFirstSevenCharacters = "You need my first seven characters"
#
###################### YOUR CODE BELOW THIS LINE #######################

firstSevenCharacters = getFirstSevenCharacters[:7]

########################################################################



########################################################################
#
#  EXERCISE 10 - STRING LAST CHARACTER
#
#  Get the last character of 'getLastCharacter' and save the result
#  into 'lastCharacter'
getLastCharacter = "You need my last character don't ya?"
#
###################### YOUR CODE BELOW THIS LINE #######################

lastCharacter = getLastCharacter[-1]

########################################################################



########################################################################
#
#  EXERCISE 11 - STRING LAST 4 CHARACTERS
#
#  Get the last four characters of 'getLastFourCharacters' and save the result
#  into 'lastFourCharacters'
getLastFourCharacters = "You need my last four characters don't ya?"
#
###################### YOUR CODE BELOW THIS LINE #######################

lastFourCharacters = getLastFourCharacters[-4:]

########################################################################



########################################################################
#
#  EXERCISE 12 - STRING EQUALS
#
#  Determine if strings 'checkEquality1' and 'checkEquality2' are equal
#  and save the result into 'stringsAreEqual'
checkEquality1 = "Are we equal?"
checkEquality2 = "Are we equal?"
#  NOTE: stringsAreEqual should be a boolean value of True or False
#
###################### YOUR CODE BELOW THIS LINE #######################

stringsAreEqual = checkEquality1 == checkEquality2
########################################################################



########################################################################
#
#  EXERCISE 13 - STRING EQUALS IGNORE CASE
#
#  Determine if strings 'checkEqualityIgnoreCase1' and 'checkEqualityIgnoreCase2'
#  are equal, ignoring case, and save the result into 'stringsAreEqualIgnoreCase'
checkEqualityIgnoreCase1 = "Are we equal?"
checkEqualityIgnoreCase2 = "are we EQUAL?"
#  NOTE: stringsAreEqualIgnoreCase should be a boolean value of True or False
#
###################### YOUR CODE BELOW THIS LINE #######################

stringsAreEqualIgnoreCase = checkEqualityIgnoreCase1.lower() == checkEqualityIgnoreCase2.lower()

########################################################################



########################################################################
#
#  EXERCISE 14 - STRING REPLACE
#
#  Replace all occurences of "John" with "Michael" in 'replaceMe' and save
#  the result into 'replacedString'
replaceMe = "John just moved to Montreal. John will be meeting his roomate soon."
#
###################### YOUR CODE BELOW THIS LINE #######################

replacedString = replaceMe.replace("John", "Michael")

########################################################################



########################################################################
#
#  EXERCISE 15 - STRING REMOVE
#
#  Remove 'going to' from the string 'removeMe' so that is makes sense
#  and save the result into removedString
#  NOTE: You can use the replace function to do so
removeMe = "We will going to be leaving at noon sharp."
#
###################### YOUR CODE BELOW THIS LINE #######################

removedString = removeMe.replace("going to ", "")

########################################################################



########################################################################
#
#  EXERCISE 16 - MULTIPLE MANIPULATIONS 1
#
#  Turn 'testString1':
testString1 = "The quick brown fox jumps over the lazy dog"
#  into 'targetString1':
targetString1 = "THE-QUICK-BROWN-FOX-JUMPS-OVER-THE-LAZY-DOG"
#  NOTE: Unlike javascript, python strings are immutable, changing a
#  string requires you to save the changed string into a new variable
#  simply do testString1 = testString1[:] etc to update the testString1
#  variable - feel free to do this in multiple steps
#
###################### YOUR CODE BELOW THIS LINE #######################
testString1 = testString1.upper().replace(" ", "-")


########################################################################



########################################################################
#
#  EXERCISE 17 - MULTIPLE MANIPULATIONS 2
#
#  Turn 'testString2':
testString2 = "I am the first sentence. You are the second sentence"
#  into 'targetString2':
targetString2 = "i am the second best, you are the first best!"
#  NOTE: Unlike javascript, python strings are immutable, changing a
#  string requires you to save the changed string into a new variable
#  simply do testString2 = testString2[:] etc to update the testString1
#  variable - feel free to do this in multiple steps
#
###################### YOUR CODE BELOW THIS LINE #######################

testString2 = testString2.lower()
testString2 = testString2.replace("first sentence", "second best")
testString2 = testString2.replace("second sentence", "first best")
testString2 = testString2.replace(".", ",")

targetString2 = testString2

########################################################################



####################### END OF STRINGS EXERCISES #######################



########################################################################
#
#								ANSWERS
#
#  DO NOT LOOK AT THIS SECTION UNTIL YOU HAVE FINISHED THE EXERCISES
#
#  The following code tests the variables you need to work on to confirm your work is
#  correct. The if conditions check the variables are correct and the console.log()
#  statements are what make the print outs you see when you run the file. The below
#  is a crude demonstration of what we refer to as code tests. Code testing is a
#  common practice in the software engineer's role, where tests are run to confirm all
#  code runs correctly. Only when all tests pass would we give ourselves the green light
#  to ship code to production and feel confident the system will perform as expected.
#
########################################################################

# setGreen instructs the shell to set the printed output to green
setGreen = "\x1b[32m"
# setRed instructs the shell to set the printed output to red
setRed = "\x1b[31m"
# resetColor instructs the shell to reset the printout color to standard
resetColor = "\x1b[0m"

# Set correctMsg and incorrectMsg Messages so I don't need to write it everytimne
correctMsg = setGreen + "Correct! " + resetColor
incorrectMsg = setRed + "Incorrect! " + resetColor

# totalTests and passedTests count the final tally of passed tests
totalTests = 0
passedTests = 0

# String Initialization
if newString == None:
	print(incorrectMsg + "The initialized 'newString' should be defined")
elif type(newString) is str and len(newString) > 1:
	print(correctMsg + "You initialized 'newString' as: '" + newString + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "The initialized 'newString' should be a non-empty string, yours is '" + newString + "'")
totalTests += 1

# String TypeOf
correctGotDataType = type(getMyDataType)
if gotDataType == None:
	print(incorrectMsg + "The initialized 'gotDataType' should be defined")
elif gotDataType == correctGotDataType:
	print(correctMsg + "The value of the 'gotDataType' variable you got was: '" + str(gotDataType) + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "The value of the 'gotDataType' variable should be '" + str(correctGotDataType) + "', yours is '" + str(gotDataType) + "'")
totalTests += 1

# String Length
correctLength = len(getMyLenght)
if myLength == None:
	print(incorrectMsg + "The 'myLength' variable should be defined")
elif myLength == correctLength:
	print(correctMsg + "The length of the 'getMyLenght' variable you got was: " + str(myLength))
	passedTests+= 1
else:
	print(incorrectMsg + "The length of the 'getMyLenght' variable should be " + str(correctLength) + " but you got " + str(myLength))
totalTests += 1

# String Concatenation
correctConcat = concat1 + concat2 + concat3
if concatStrings == None:
	print(incorrectMsg + "The 'concatStrings' variable should be defined")
elif concatStrings == correctConcat:
	print(correctMsg + "The value of 'concatStrings' you got was: '" + concatStrings + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "The value of the 'concatStrings' variable should be '" + correctConcat + "' but you got '" + concatStrings + "'")
totalTests += 1

# String Repetition
correctRepeat = repeatMe * repeatTimes
if repeatedString == None:
	print(incorrectMsg + "The 'repeatedString' variable should be defined")
elif repeatedString == correctRepeat:
	print(correctMsg + "The value of 'repeatedString' you got was: '" + repeatedString + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "The value of the 'repeatedString' variable should be '" + correctRepeat + "' but you got '" + repeatedString + "'")
totalTests += 1

# String Contains
correctContains = subString in mainString
if stringContains == None:
	print(incorrectMsg + "The 'stringContains' variable should be defined")
elif stringContains == correctContains:
	print(correctMsg + "The value of 'stringContains' you got was: " + str(stringContains))
	passedTests+= 1
else:
	print(incorrectMsg + "The value of the 'stringContains' variable should be " + str(correctContains) + " but you got " + str(stringContains))
totalTests += 1

# String Find
correctFoundIndex = findSubstring.find(subStringToFind)
if foundSubstringIndex == None:
	print(incorrectMsg + "The 'foundSubstringIndex' variable should be defined")
elif foundSubstringIndex == correctFoundIndex:
	print(correctMsg + "The index of substring 'subStringToFind' in 'findSubstring' you got was: " + str(foundSubstringIndex))
	passedTests+= 1
else:
	print(incorrectMsg + "The index of substring 'subStringToFind' in 'findSubstring' should be " + str(correctFoundIndex) + " but you got " + str(foundSubstringIndex))
totalTests += 1

# String First Character
correctFirstCharacter = getFirstCharacter[0]
if firstCharacter == None:
	print(incorrectMsg + "The 'firstCharacter' variable should be defined")
elif firstCharacter == correctFirstCharacter:
	print(correctMsg + "The first character of 'getFirstCharacter' you got was: '" + firstCharacter + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "The first character of 'getFirstCharacter' should be '" + correctFirstCharacter + "' but you got '" + firstCharacter + "'")
totalTests += 1

# String First Seven Characters
correctFirstSevenCharacters = getFirstSevenCharacters[0:7]
if firstSevenCharacters == None:
	print(incorrectMsg + "The 'firstSevenCharacters' variable should be defined")
elif firstSevenCharacters == correctFirstSevenCharacters:
	print(correctMsg + "The first seven characters of 'getFirstSevenCharacters' you got was: '" + firstSevenCharacters + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "The first seven characters of 'getFirstSevenCharacters' should be '" + correctFirstSevenCharacters + "' but you got '" + firstSevenCharacters + "'")
totalTests += 1

# String Last Character
correctLastCharacter = getLastCharacter[-1]
if lastCharacter == None:
	print(incorrectMsg + "The 'lastCharacter' variable should be defined")
elif lastCharacter == correctLastCharacter:
	print(correctMsg + "The last character of 'getLastCharacter' you got was: '" + lastCharacter + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "The last character of 'getLastCharacter' should be '" + correctLastCharacter + "' but you got '" + lastCharacter + "'")
totalTests += 1

# String Last Four Characters
correctLastFourCharacters = getLastFourCharacters[-4:]
if lastFourCharacters == None:
	print(incorrectMsg + "The 'lastFourCharacters' variable should be defined")
elif lastFourCharacters == correctLastFourCharacters:
	print(correctMsg + "The last four characters of 'getLastFourCharacters' you got was: '" + lastFourCharacters + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "The last four characters of 'getLastFourCharacters' should be '" + correctLastFourCharacters + "' but you got '" + lastFourCharacters + "'")
totalTests += 1

# String Equals
correctStringEquals = checkEquality1 == checkEquality2
if stringsAreEqual == None:
	print(incorrectMsg + "The 'stringsAreEqual' variable should be defined")
elif stringsAreEqual == correctStringEquals:
	print(correctMsg + "As for strings 'checkEquality1' and 'checkEquality1' being equal, you said this was: " + str(stringsAreEqual))
	passedTests+= 1
else:
	print(incorrectMsg + "As for strings 'checkEquality1' and 'checkEquality1' being equal, this should be " + str(correctStringEquals) + " but you got " + str(stringsAreEqual))
totalTests += 1

# String Equals Ignore Case
correctStringEqualsIgnoreCase = checkEqualityIgnoreCase1.upper() == checkEqualityIgnoreCase2.upper()
if stringsAreEqualIgnoreCase == None:
	print(incorrectMsg + "The 'stringsAreEqualIgnoreCase' variable should be defined")
elif stringsAreEqualIgnoreCase == correctStringEqualsIgnoreCase:
	print(correctMsg + "As for strings 'checkEqualityIgnoreCase1' and 'checkEqualityIgnoreCase2' being equal ignoring case, you said this was: " + str(stringsAreEqualIgnoreCase))
	passedTests+= 1
else:
	print(incorrectMsg + "As for strings 'checkEqualityIgnoreCase1' and 'checkEqualityIgnoreCase2' being equal ignoring case, this should be " + str(correctStringEqualsIgnoreCase) + " but you got " + str(stringsAreEqualIgnoreCase))
totalTests += 1

# String Replace
correctReplace = replaceMe.replace("John", "Michael")
if replacedString == None:
	print(incorrectMsg + "The 'replacedString' variable should be defined")
elif replacedString == correctReplace:
	print(correctMsg + "After replacing John with Michael, your 'replacedString' looks like: '" + replacedString + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "After replacing John with Michael, your 'replacedString' should be '" + correctReplace + "' but you got '" + replacedString + "'")
totalTests += 1

# String Remove
correctRemove = removeMe.replace("going to ", "")
if removedString == None:
	print(incorrectMsg + "The 'removedString' variable should be defined")
elif removedString == correctRemove:
	print(correctMsg + "After removing \"going to\" from 'removeMe' your 'removedString' looks like: '" + removedString + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "After removing \"going to\" from 'removeMe' your 'removedString' should be '" + correctRemove + "' but you got '" + removedString + "'")
totalTests += 1

# Multiple Manipulations 1
# Since we already have a targetString1, we don't need to create a correct test variable
# correctManipulation = (testString1[0:testString1.find("dog")] + "blue " + testString1[testString1.find("dog"):]).replace(" ", "-").upper()
if testString1 == None:
	print(incorrectMsg + "The 'testString1' variable should be defined")
elif testString1 == targetString1:
	print(correctMsg + "After your manipulations to 'testString1', 'manipulatedString1' now looks like: '" + testString1 + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "After your manipulations to 'testString1', it should be '" + targetString1 + "' but you got '" + testString1 + "'")
totalTests += 1

# Multiple Manipulations 2
# Since we already have a targetString2, we don't need to create a correct test variable
# correctManipulation = testString2.lower().replace("first sentence.", "second best,").replace("second sentence", "first best") + "!"
if testString2 == None:
	print(incorrectMsg + "The 'targetString2' variable should be defined")
elif testString2 == targetString2:
	print(correctMsg + "After your manipulations to 'testString2', 'manipulatedString1' now looks like: '" + testString2 + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "After your manipulations to 'testString2', it should be '" + targetString2 + "' but you got '" + testString2 + "'")
totalTests += 1

# Final Test Tally Determination
if passedTests == totalTests:
	print(setGreen + "You passed " + str(passedTests) + " / " + str(totalTests) + " tests. Congratulations!" + resetColor)
else:
	print(setRed + "You passed " + str(passedTests) + " / " + str(totalTests) + " tests. Keep Going!" + resetColor)