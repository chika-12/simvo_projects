########################################################################
#
#  EXERCISE 1 - INTEGER INITALIZATION
#
#  Initialize the 'newInteger' variable as any kind of INTEGER
#
###################### YOUR CODE BELOW THIS LINE #######################

newInteger = 89

########################################################################



########################################################################
#
#  EXERCISE 2 - FLOAT INITALIZATION
#
#  Initialize the 'newFloat' variable as any kind of FLOAT
#
###################### YOUR CODE BELOW THIS LINE #######################

newFloat = 23.339

########################################################################



########################################################################
#
#  EXERCISE 3 - IS INTEGER
#
#  Check if variable 'integer1' is an integer and save the result into
#  'integer1IsInteger'
integer1 = "Not an integer"
#  NOTE: integer1IsInteger should be a boolean value of True or False
#
###################### YOUR CODE BELOW THIS LINE #######################

integer1IsInteger = isinstance(integer1, int)

########################################################################



########################################################################
#
#  EXERCISE 4 - IS FLOAT
#
#  Check if variable 'float1' is a float and save the result into
#  'float1IsFloat'
float1 = 45.6
#  NOTE: float1IsFloat should be a boolean value of True or False
#
###################### YOUR CODE BELOW THIS LINE #######################

float1IsFloat = isinstance(float1, float)

########################################################################



########################################################################
#
#  EXERCISE 5 - ABSOLUTE VALUE
#
#  Get the absolute value of 'getMyAbsoluteValue' and save the result
#  into 'absoluteValue'
getMyAbsoluteValue = -64.4
#
###################### YOUR CODE BELOW THIS LINE #######################

absoluteValue = abs(getMyAbsoluteValue)

########################################################################



########################################################################
#
#  EXERCISE 6 - ROUND UP A NUMBER
#
#  Round up the variable 'roundMeUp' to the nearest integer and save the
#  the result into 'roundedUpNumber'
roundMeUp = 85.4
#  NOTE: You will need to use the Mathematics module 'math' imported
#  below for you
import math
#
###################### YOUR CODE BELOW THIS LINE #######################

roundedUpNumber = math.ceil(roundMeUp)

########################################################################



########################################################################
#
#  EXERCISE 7 - ROUND DOWN A NUMBER
#
#  Round down the variable 'roundMeDown' to the nearest integer and save the
#  the result into 'roundedDownNumber'
roundMeDown = 85.4
#  NOTE: You will need to use the Mathematics module 'math' imported
#  in the previous exercise for you
#
###################### YOUR CODE BELOW THIS LINE #######################

roundedDownNumber = math.floor(roundMeDown)

########################################################################



########################################################################
#
#  EXERCISE 8 - NUMBER TO THE POWER
#
#  Calculate 'baseNumber' to the power of 'powerNumber' and save the
#  result into 'baseToThePower'
baseNumber = 4
powerNumber = 5
#
###################### YOUR CODE BELOW THIS LINE #######################

baseToThePower = baseNumber ** powerNumber

########################################################################



########################################################################
#
#  EXERCISE 9 - PERCENTAGE CALCULATION TO 3 DECIMAL PLACES
#
#  Calculate the percentage of 'scoreValue' out of 'maxValue' to
#  3 decimal places and save the result into 'scorePercentage'
scoreValue = 23.5
maxValue = 35
#
###################### YOUR CODE BELOW THIS LINE #######################

scorePercentage = round((scoreValue / maxValue) * 100, 3)

########################################################################



########################################################################
#
#  EXERCISE 10 - Add number to string
#
#  Add the number in variable 'score' to the end of the string variable
#  'messagePrefix' and save it into the variable 'scoreMessage'
messagePrefix = "You got a score of"
score = 145
#
###################### YOUR CODE BELOW THIS LINE ######################

scoreMessage = messagePrefix + " " + str(score)

########################################################################



########################################################################
#
#  EXERCISE 9 - Parse float from string
#
#  Parse the number from string variable 'parseTheNumber' and save it into
#  'parsedNumber' which should be of number data type
parseTheNumber = "Prerequisite score of 50.5 is required to pass"
#  NOTE: You will need to use the imported regular expression module 're'
#  imported below for you
import re
#
###################### YOUR CODE BELOW THIS LINE ######################

parsedNumber = float(re.search(r"\d+(\.\d+)?", parseTheNumber).group())

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

# Integer Initialization
if newInteger == None:
	print(incorrectMsg + "The initialized 'newInteger' should be defined")
elif type(newInteger) is int:
	print(correctMsg + "You initialized 'newInteger' as: '" + str(newInteger))
	passedTests+= 1
else:
	print(incorrectMsg + "The initialized 'newInteger' should be an integer, yours is " +	str(type(newInteger)))
totalTests += 1

# Float Initialization
if newFloat == None:
	print(incorrectMsg + "The initialized 'newFloat' should be defined")
elif type(newFloat) is float:
	print(correctMsg + "You initialized 'newFloat' as '" + str(newFloat))
	passedTests+= 1
else:
	print(incorrectMsg + "The initialized 'newFloat' should be a float, yours is " +	str(type(newFloat)))
totalTests += 1

# Is Integer
correctInteger1IsInteger = type(integer1) is int
if integer1IsInteger == None:
	print(incorrectMsg + "The 'integer1IsInteger' variable should be defined")
elif integer1IsInteger == correctInteger1IsInteger:
	print(correctMsg + "As for the variable 'integer1' being an integer, you found this was " + str(integer1IsInteger))
	passedTests+= 1
else:
	print(incorrectMsg + "As for the variable 'integer1' being an integer, this should be " + str(correctInteger1IsInteger) + " but you got " + str(integer1IsInteger))
totalTests += 1

# Is Float
correctFloat1IsFloat = type(float1) is float
if float1IsFloat == None:
	print(incorrectMsg + "The 'float1IsFloat' variable should be defined")
elif float1IsFloat == correctFloat1IsFloat:
	print(correctMsg + "As for the variable 'float1' being a float, you found this was " + str(float1IsFloat))
	passedTests+= 1
else:
	print(incorrectMsg + "As for the variable 'float1' being a float, this should be " + str(correctFloat1IsFloat) + " but you got " + str(float1IsFloat))
totalTests += 1

# Absolute Value
correctAbsoluteValue = abs(getMyAbsoluteValue)
if absoluteValue == None:
	print(incorrectMsg + "The 'absoluteValue' variable should be defined")
elif absoluteValue == correctAbsoluteValue:
	print(correctMsg + "The absolute value of 'getMyAbsoluteValue' you got was " + str(absoluteValue))
	passedTests+= 1
else:
	print(incorrectMsg + "The absolute value of 'getMyAbsoluteValue' should be " + str(correctAbsoluteValue) + " but you got " + str(absoluteValue))
totalTests += 1

# Round Up A Number
correctRoundedUpNumber = math.ceil(roundMeUp)
if roundedUpNumber == None:
	print(incorrectMsg + "The 'roundedUpNumber' variable should be defined")
elif roundedUpNumber == correctRoundedUpNumber:
	print(correctMsg + "The rounded up number of 'roundMeUp' you got was " + str(roundedUpNumber))
	passedTests+= 1
else:
	print(incorrectMsg + "The rounded up number of 'roundMeUp' should be " + str(correctRoundedUpNumber) + " but you got " + str(roundedUpNumber))
totalTests += 1

# Round Down A Number
correctRoundedDownNumber = math.floor(roundMeDown)
if roundedDownNumber == None:
	print(incorrectMsg + "The 'roundedDownNumber' variable should be defined")
elif roundedDownNumber == correctRoundedDownNumber:
	print(correctMsg + "The rounded down number of 'roundMeDown' you got was " + str(roundedDownNumber))
	passedTests+= 1
else:
	print(incorrectMsg + "The rounded down number of 'roundMeDown' should be " + str(correctRoundedDownNumber) + " but you got " + str(roundedDownNumber))
totalTests += 1

# Number To The Power
correctBaseToThePower = baseNumber**powerNumber
if baseToThePower == None:
	print(incorrectMsg + "The 'roundedDownNumber' variable should be defined")
elif baseToThePower == correctBaseToThePower:
	print(correctMsg + "The 'baseNumber' to the power of 'powerNumber' you got was " + str(baseToThePower))
	passedTests+= 1
else:
	print(incorrectMsg + "The 'baseNumber' to the power of 'powerNumber' should be " + str(correctBaseToThePower) + " but you got " + str(baseToThePower))
totalTests += 1

# Percentage Calculation To 3 Decimal Places
correctScorePercentage = round((100 * scoreValue / maxValue), 3)
if scorePercentage == None:
	print(incorrectMsg + "The 'scorePercentage' variable should be defined")
elif scorePercentage == correctScorePercentage:
	print(correctMsg + "The percentage of 'scoreValue' out of 'maxValue' to 3 decimal places you got was " + str(scorePercentage))
	passedTests+= 1
else:
	print(incorrectMsg + "The percentage of 'scoreValue' out of 'maxValue' to 3 decimal places should be " + str(correctScorePercentage) + " but you got " + str(scorePercentage))
totalTests += 1

# Add number to string
correctScoreMessage =	messagePrefix + " " + str(score)
if scoreMessage == None:
	print(incorrectMsg + "The 'scoreMessage' variable should be defined")
elif scoreMessage == correctScoreMessage:
	print(correctMsg + "The value of 'scoreMessage' you got was " + scoreMessage)
	passedTests+= 1
else:
	print(incorrectMsg + "The value of 'scoreMessage' should be " + correctScoreMessage + " but you got " + scoreMessage)
totalTests += 1

# Parse number from string
correctParsedNumber = float(re.sub(r'[^0-9.]', "", parseTheNumber))
if parsedNumber == None:
	print(incorrectMsg + "The 'parsedNumber' variable should be defined")
elif parsedNumber == correctParsedNumber:
	print(correctMsg + "The value of 'parsedNumber' you got was " + str(parsedNumber))
	passedTests+= 1
else:
	print(incorrectMsg + "The value of 'parsedNumber' should be " + str(correctParsedNumber) + " of type " + str(type(correctParsedNumber)) + " but you got " + str(parsedNumber)	+ " of type " + str(type(parsedNumber)))
totalTests += 1

# Final Test Tally Determination
if passedTests == totalTests:
	print(setGreen + "You passed " + str(passedTests) + " / " + str(totalTests) + " tests. Congratulations!" + resetColor)
else:
	print(setRed + "You passed " + str(passedTests) + " / " + str(totalTests) + " tests. Keep Going!" + resetColor)