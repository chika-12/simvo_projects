########################################################################
#
#  EXERCISE 1 - INITALIZATION
#
#  Initialize the 'newBoolean' variable as a boolean literal of value False
#
###################### YOUR CODE BELOW THIS LINE #######################

newBoolean = False

########################################################################



########################################################################
#
#  EXERCISE 2 - DO I PASS THIS COURSE
#
#  To graduate, the student needs at least one of their exams to be above 75%
#  pass mark. Check to see if the student passes at least one of their exams
#  ('examScore1' and 'examScore2') and save the result into 'studentPasses'
#
import random
examScore1 = random.randint(0, 100)
examScore2 = random.randint(0, 100)
scoreToPass = 75
#
###################### YOUR CODE BELOW THIS LINE #######################

studentPasses = examScore1 >= scoreToPass or examScore2 >= scoreToPass

########################################################################



########################################################################
#
#  EXERCISE 3 - HOW MUCH WOOD WOULD A WOODCHUCK CHUCK?
#
#  Two children were asked to guess how many times the characters "wood"
#  and "chuck" (but NOT in the word "woodchuck") appeared in the famous
#  'tongueTwiser'. You have two tasks:
#  - Get the correct number of times "wood" and "chuck" appeared in 'tongueTwiser',
#    not including in "woodchuck", and save them into 'numberOfWood' and 'numberOfChuck' respectively
#  - Confirm they BOTH GOT AT LEAST ONE GUESS CORRECT for either
#    occurence of "wood" or "chuck" and save it into 'bothAtLeastOneCorrect'
#
# tongueTwiser was concatenated like this so the string does not go out of view
tongueTwiser = "How much wood would a woodchuck chuck if a woodchuck could chuck wood? "
tongueTwiser += "He would chuck, he would, as much as he could, and chuck as much wood, "
tongueTwiser += "as a woodchuck would if a woodchuck could chuck wood."
# Student 1's guesses
student1Wood = random.randint(3, 5)
student1Chuck = random.randint(4, 6)
# Student 2's guesses
student2Wood = random.randint(3, 5)
student2Chuck = random.randint(4, 6)
#
###################### YOUR CODE BELOW THIS LINE #######################
modifiedTwister = tongueTwiser.replace("woodchuck", "")
numberOfWood = modifiedTwister.count("wood")
numberOfChuck = modifiedTwister.count("chuck")

bothAtLeastOneCorrect = (
	(student1Wood == numberOfWood or student1Chuck == numberOfChuck)
	and
	(student2Chuck == numberOfWood or student2Chuck == numberOfChuck)
)

########################################################################



########################################################################
#
#  EXERCISE 4 - TRUTHY AND FALSY
#
#  As well as a type, each value also has an inherent boolean value,
#  generally known as either truthy or falsy. Some of the rules are a
#  little bizarre so have a look at the following conversions using
#  the bool() conversion function, which will look at the non-boolean
#  data types and return their inherent boolean value
#
falsy1 = falsy2 = falsy3 = None
truthy1 = truthy2 = None
# Uncomment the lines below to see what they evaluate to
#
###################### YOUR CODE BELOW THIS LINE #######################

falsy1 = bool("")
falsy2 = bool(0)
falsy3 = bool(None)

truthy1 = bool("non-empty string")
truthy2 = bool(1)

########################################################################



###################### END OF BOOLEANS EXERCISES #######################



########################################################################
#
#                               ANSWERS
#
#  DO NOT LOOK AT THIS SECTION UNTIL YOU HAVE FINISHED THE EXERCISES
#
#  The following code tests the variables you need to work on to confirm your work is
#  correct. The if conditions check the variables are correct and the print()
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


# Boolean Initialization
if newBoolean == None:
	print(incorrectMsg + "The initialized 'newBoolean' variable should be defined")
elif type(newBoolean) is bool and not newBoolean:
	print(correctMsg + "The value of 'newBoolean' you got was: '" + str(newBoolean) + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "The value of 'newBoolean' should be 'False', yours is '" + str(newBoolean) + "'")
totalTests += 1


# Do I pass The Course
correctStudentPasses = examScore1 >= scoreToPass or examScore2 >= scoreToPass
if studentPasses == None:
	print(incorrectMsg + "The initialized 'studentPasses' variable should be defined")
elif type(studentPasses) is bool and studentPasses == correctStudentPasses:
	print(correctMsg + "Passed exam score tests")
	print("\tThe students two scores on the test were " + str(examScore1) + " and " + str(examScore2) + ", the score to pass was " + str(scoreToPass) + ".")
	print("\tThe value of 'studentPasses' you got was: '" + str(studentPasses) + "'")
	passedTests+= 1
else:
	print(incorrectMsg + "Failed exam score tests")
	print("\tThe students two scores on the test were " + str(examScore1) + " and " + str(examScore2) + ", the score to pass was " + str(scoreToPass) + ".")
	print("\tThe value of 'studentPasses' should be '" + str(correctStudentPasses) + "', yours is '" + str(studentPasses) + "'")
totalTests += 1


# How Much Wood Would a Woodchuck Chuck
correctNumberOfWood = tongueTwiser.count("wood ") + tongueTwiser.count("wood.") + tongueTwiser.count("wood?") + tongueTwiser.count("wood,")
correctNumberOfChuck = tongueTwiser.count(" chuck")
correctBothAtLeast = (student1Chuck == correctNumberOfChuck or student1Wood == correctNumberOfWood) and (student2Chuck == correctNumberOfChuck or student2Wood == correctNumberOfWood)
if numberOfWood == None or numberOfChuck == None or bothAtLeastOneCorrect == None:
	print(incorrectMsg + "The initialized 'numberOfWood', 'numberOfChuck' and 'bothAtLeastOneCorrect' variables should be defined")
elif numberOfWood == correctNumberOfWood and numberOfChuck == correctNumberOfChuck and type(bothAtLeastOneCorrect) is bool and bothAtLeastOneCorrect == correctBothAtLeast:
	print(correctMsg + "There were exactly " + str(correctNumberOfWood) + " woods and " + str(correctNumberOfChuck) + " chucks in the sentence.")
	print("\tYou said there were " + str(numberOfWood) + " woods and " + str(numberOfChuck) + " chucks in the sentence.")
	print("\tStudent 1 guessed " + str(student1Wood) + " woods and " + str(student1Chuck) + " chucks!")
	print("\tStudent 2 guessed " + str(student2Wood) + " woods and " + str(student2Chuck) + " chucks!")
	print("\tThe value of 'bothAtLeastOneCorrect' you got was thus: '" + str(bothAtLeastOneCorrect) + "' on whether both had at least one answer correct")
	passedTests+= 1
else:
	print(incorrectMsg + "There were exactly " + str(correctNumberOfWood) + " woods and " + str(correctNumberOfChuck) + " chucks in the sentence.")
	print("\tYou said there were " + str(numberOfWood) + " woods and " + str(numberOfChuck) + " chucks in the sentence.")
	print("\tStudent 1 guessed " + str(student1Wood) + " woods and " + str(student1Chuck) + " chucks!")
	print("\tStudent 2 guessed " + str(student2Wood) + " woods and " + str(student2Chuck) + " chucks!")
	print("\tThe value of 'bothAtLeastOneCorrect' should thus be '" + str(correctBothAtLeast) +  "' but you got '" + str(bothAtLeastOneCorrect) + "'")
totalTests += 1


# Truty and Falsy Values
if falsy1 == None or falsy2 == None or falsy3 == None or truthy1 == None or truthy2 == None:
	print(incorrectMsg + "The initialized 'falsy1', 'falsy2', 'falsy3', 'falsy4', 'truthy1', and 'truthy2' variables should be defined")
elif not falsy1 and not falsy2 and not falsy3 and truthy1 and truthy2:
	print(correctMsg + "Passed falsy and truthy values:")
	print("\tFalsy values:")
	print('\tThe expression [ bool("") ]          evaluates to ' + str(falsy1))
	print('\tThe expression [ bool(0) ]           evaluates to ' + str(falsy2))
	print('\tThe expression [ bool(None) ]        evaluates to ' + str(falsy3))
	print("\tTruthy values:")
	print('\tThe expression [ bool("non-empty") ] evaluates to ' + str(truthy1))
	print('\tThe expression [ bool(1) ]           evaluates to ' + str(truthy2))
	passedTests+= 1
else:
	print(incorrectMsg + "Failed falsy and truthy values:")
	print("\tFalsy values:")
	print("\tThe expression [ bool(\"\") ] should be saved into 'falsy1'")
	print("\tThe expression [ bool(0) ] should be saved into 'falsy2'")
	print("\tThe expression [ bool(None) ] should be saved into 'falsy3'")
	print("\tTruthy values:")
	print("\tThe expression [ bool(\"non-empty\") ] should be saved into 'truthy1'")
	print("\tThe expression [ bool(1) ] should be saved into 'truthy2'")
totalTests += 1


# Final Test Tally Determination
if passedTests == totalTests:
	print(setGreen + "You passed " + str(passedTests) + " / " + str(totalTests) + " tests. Congratulations!" + resetColor)
else:
	print(setRed + "You passed " + str(passedTests) + " / " + str(totalTests) + " tests. Keep Going!" + resetColor)