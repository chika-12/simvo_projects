########################################################################
#
#  EXERCISE 1 - INITALIZATION
#
#  Initialize the 'newDict' variable with one key called "key"
#  that has a value which is a string called "value", it should look like:
#  {
#	"key": "value"
#  }
#
###################### YOUR CODE BELOW THIS LINE #######################

newDict = {
 			"key": "value"
		  }

########################################################################



########################################################################
#
#  EXERCISE 2 - GET MY AGE
#
#  The 'getMyAge' dictionary contains my date of birth stored as year, month
#  and day.
import random
getMyAge = {
	"name": "John Nnamchi",
	"DOB": {
		"year": random.randint(1960, 2005),
		"month": random.randint(1, 12),
		"day": random.randint(1, 30),
	}
}
#  Your objective is to use the datetime data type to create a new date
#  with the year, month and day keys of the 'getMyAge' 'DOB' object and
#  determine how old this person is in days, months and years saved into
#  'ageInDays', 'ageInMonths' and 'ageInYears' respectively
#  Hint: The solution requires the inbuilt datetime module imported below
#  There is nothing complicated about this data type, in
#  fact this data type makes life much easier when working with date:
import datetime
#
###################### YOUR CODE BELOW THIS LINE #######################

dob = datetime.date(
    getMyAge["DOB"]["year"],
    getMyAge["DOB"]["month"],
    getMyAge["DOB"]["day"]
)

today = datetime.date.today()

ageInDays = (today - dob).days
ageInMonths = ageInDays / 12
ageInYears = ageInDays / 365
########################################################################



########################################################################
#
#  EXERCISE 3 - DEEP COPY
#
#  The 'deepDictionary' dictionary contains my date of birth stored as the python
#  datetime data type. There is nothing complicated about this data type, in
#  fact this data type makes life much easier when working with date:
deepDictionary = {
	"name": "Jeans Immons",
	"age": random.randint(15, 40),
	"siblings": [
		"Michael",
		"Alex",
		"Charles",
	]
}
#  Your objective is make a copy of 'deepDictionary' saved into 'deepDictionaryCopy'
#  and then do the following to 'deepDictionaryCopy':
#  - Change the name of 'deepDictionaryCopy' to "Kravis Lott"
#  - Leave the age unchanged
#  - Remove the last element from the "sibblings" list
#  Since 'deepDictionaryCopy' a copy it should leave 'deepDictionary' untouched
#  Hint: The solution requires the inbuilt copy module imported below
import copy
#
###################### YOUR CODE BELOW THIS LINE #######################

deepDictionaryCopy = copy.deepcopy(deepDictionary)

deepDictionaryCopy["name"] = "Kravis Lott"

deepDictionaryCopy["siblings"].pop()

########################################################################



########################################################################
#
#  EXERCISE 4 - DICT MANIPULATION
#
#  The following 'student' dictionary representing a student is out of date:
studentGrade = random.randint(5, 11)
studentGPA = round(random.uniform(3, 4), 2)
student = {
	"name": "Christian Ronald",
	"grade": studentGrade,
	"gpa": studentGPA,
	"courses": [
		{
			"subject": "ENG",
			"level": 101,
		}
	]
}
#  Manipulate the student dictionary to reflect the following changes:
#  - They have moved up one grade
#  - Their GPA has dropped by 0.15 points
#  - They have taken a new course: MATH 204
#  - They got their first absence, add a new key called "absences" to
#	their record with a value of 1
#
#  Ignore the student copy dictionary below, it is used to check you work
studentCopy = dict(student)
#
###################### YOUR CODE BELOW THIS LINE #######################

student["grade"] += 1

student["gpa"] -= 0.15

student["courses"].append({
    "subject": "MATH",
    "level": 204
})

student["absences"] = 1

########################################################################



# ##################### END OF DICTIONARY EXERCISES ######################



########################################################################
#
#							   ANSWERS
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

import json

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

# Add print statement so its easy to scroll to top of exercises
print("+----------------------------------+")
print("|                                  |")
print("|       EXERCISES START HERE       |")
print("|                                  |")
print("+----------------------------------+")
print("")

# Dict Initialization
correctNewDict = {
	"key": "value"
}
if newDict == None:
	print(incorrectMsg + "The initialized 'newDict' variable should be defined")
elif type(newDict) is dict and newDict == correctNewDict:
	print(correctMsg + "The value of 'newDict' you got was:")
	print(json.dumps(newDict, indent=2))
	passedTests += 1
else:
	print(incorrectMsg + "'newDict' should be an dictionary that looks like:")
	print(json.dumps(correctNewDict, indent=2))
	print("but yours looks like:")
	print(json.dumps(newDict, indent=2))
totalTests += 1
print("")

# Get My Age
correctDOB = datetime.date(getMyAge["DOB"]["year"], getMyAge["DOB"]["month"], getMyAge["DOB"]["day"])
correctAgeInDays = (datetime.date.today() - correctDOB).days
correctgAgeInMonths = correctAgeInDays / 12
correctAgeInYears = correctAgeInDays / 365
if ageInDays == None or ageInMonths == None or ageInYears == None:
	print(incorrectMsg + "The initialized 'ageInDays', 'ageInMonths' and 'ageInYeaars' variables should all be defined")
elif ageInDays == correctAgeInDays and ageInMonths == correctgAgeInMonths and ageInYears == correctAgeInYears:
	print(correctMsg + "The 'getMyAge' dictionary looked like:")
	print(json.dumps(getMyAge, indent=2))
	print("and you said they were:")
	print(str(ageInDays) + " days old")
	print(str(ageInMonths) + " months old")
	print(str(ageInYears) + " years old")
	passedTests += 1
else:
	print(incorrectMsg + "The 'getMyAge' dictionary looked like:")
	print(json.dumps(getMyAge, indent=2))
	print("and they should be:")
	print(str(correctAgeInDays) + " days old but you said they were " + str(ageInDays) + " days old")
	print(str(correctgAgeInMonths) + " months old but you said they were " + str(ageInMonths) + " months old")
	print(str(correctAgeInYears) + " years old but you said they were " + str(ageInYears) + " years old")
totalTests += 1
print("")

# Dict Deep Copy
correctDeepDictionaryCopy = {
	"name": "Kravis Lott",
	"age": deepDictionary["age"],
	"siblings": [ "Michael", "Alex" ]
}
correctSiblings = [ "Michael", "Alex", "Charles" ]
if deepDictionaryCopy == None:
	print(incorrectMsg + "The initialized 'deepDictionaryCopy' variable should be defined")
elif type(deepDictionaryCopy) is dict and deepDictionaryCopy == correctDeepDictionaryCopy:
	if deepDictionary["siblings"] == correctSiblings and deepDictionary["name"] == "Jeans Immons":
		print(correctMsg + "After your changes the 'deepDictionaryCopy' dictionary looked like:")
		print(json.dumps(deepDictionaryCopy, indent=2))
		print("while 'deepDictionary' remained unchanged as:")
		print(json.dumps(deepDictionary, indent=2))
		passedTests += 1
	else:
		print(incorrectMsg + "The 'deepDictionaryCopy' changes were correct and look like:")
		print(json.dumps(deepDictionaryCopy, indent=2))
		print("but you also edited the original 'deepDictionary' which now looks like:")
		print(json.dumps(deepDictionary, indent=2))
else:
	print(incorrectMsg + "After changes made to 'deepDictionaryCopy' it should look like:")
	print(json.dumps(correctDeepDictionaryCopy, indent=2))
	print("but it looks like:")
	print(json.dumps(deepDictionaryCopy, indent=2))
totalTests += 1
print("")

# Dict Manipulation
studentCopy["grade"] += 1
studentCopy["gpa"] -= 0.15
studentCopy["courses"].append({
	"subject": "MATH",
	"level": 204,
})
studentCopy["absences"] = 1
if student == None:
	print(incorrectMsg + "The initialized 'student' dictionary should be defined")
elif type(student) is dict and student == studentCopy:
	print(correctMsg + "After making the changes to 'student' it looks like:")
	print(json.dumps(student, indent=2))
	passedTests += 1
else:
	print(incorrectMsg + "There are one or multiple changes to 'student' that are not correct, it should look like:")
	print(json.dumps(studentCopy, indent=2))
	print("but yours looks like:")
	print(json.dumps(student, indent=2))
totalTests += 1
print("")

# Final Test Tally Determination
if passedTests == totalTests:
	print(setGreen + "You passed " + str(passedTests) + " / " + str(totalTests) + " tests. Congratulations!" + resetColor)
else:
	print(setRed + "You passed " + str(passedTests) + " / " + str(totalTests) + " tests. Keep Going!" + resetColor)