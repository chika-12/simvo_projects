////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 1 - INITALIZATION
//
//	Mapping capabilities in javascript are implement using the Object data
//	type. Initialize the 'newObject' variable with one key called "key"
//	that has a value which is a string called "value", it should look like:
//	{
//		key: "value"
//	}
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let newObject = {
	key: "value"
}

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 2 - ADD NEW KEY VALUE PAIR
//
//	Add a new key value pair to the 'addNewKVPair' object. Give the
//	new key a name of "two" and give it a value of 2, an integer
let addNewKVPair = {
	one: 1
}
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////
addNewKVPair.two = 2


////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 3 - GET VALUE OF KEY
//
//	Get the age of 'getPatientAge' and save the result into 'patientAge'
let getPatientAge = {
	name: "John Nnamchi",
	age: generateRandomNumber(18, 30),
	pastConditions: [ "fever", "headache" ]
}
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let patientAge = getPatientAge["age"]

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 4 - OBJECT MANIPULATION
//
//	The 'patient' object needs to be kept up to date.
let patient = {
	name: "John Nnamchi",
	age: generateRandomNumber(18, 30),
	pastConditions: [ "fever", "headache" ],
	hobbies: [ "TV", "Frisbee" ]
}
//	Since the last entry:
//	- John is now one year older
//	- John got a case of "vomiting"
//	- John has stopped watching TV
//	Edit the patient object to reflect these new changes
//
//	NOTE: The below 'patientCopy' is required for checking your work due
//	to some fields being randomly generated. Please do not touch this!
let patientCopy = JSON.parse(JSON.stringify(patient))
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

patient.age+= 1
patient.hobbies.shift()
patient.pastConditions.push("vomiting")
////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 5 - CONTAINS KEY
//
//	Check if 'checkContains' contains the key 'hobbies', and save the
//	result into 'containsHobbies'
let checkContains = generateRandomObject()
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let containsHobbies = "hobbies" in checkContains

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 6 - SORTED KEYS
//
//	Get the list of keys in 'sortMyKeys' and save the result
//	into 'sortedKeys' as an array of keys, then sort 'sortedKeys' alphabetically
let sortMyKeys = {
	name: "John Nnamchi",
	age: 23,
	pastConditions: [ "fever", "headache" ],
	hobbies: [ "TV", "Frisbee" ],
	born: new Date(1996, 7, 20),
	isNewPatient: false,
	height: 183,
	weight: 80,
	remarks: "Very calm individual who listens to doctor's advice"
}
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let sortedKeys = Object.keys(sortMyKeys).sort()

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 7 - CLEAR OBJECT
//
//	Remove all keys from 'clearMe' so that it no longer has any keys
//	and looks like {}
let clearMe = {
	name: "John Nnamchi",
	age: 23,
	pastConditions: [ "fever", "headache" ],
	hobbies: [ "TV", "Frisbee" ],
	born: new Date(1996, 7, 20),
	isNewPatient: false,
	height: 183,
	weight: 80,
	remarks: "Very calm individual who listens to doctor's advice"
}
//
//	The 'clearMeCopy' holds the same reference to the 'clearMe' object, so
//	that we can ensure you clear the object properly
let clearMeCopy = clearMe
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////
	for (let key in clearMe) {
		delete clearMe[key]
	}


////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 8 - OBJECT IS EMPTY
//
//	Check if the object 'emptyObject' is empty, ie has no keys, and save
//	the result into 'isEmpty'
let emptyObject = generateRandomEmptyObject()
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let isEmpty = Object.keys(emptyObject).length === 0

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 9 - DEEP OBJECT 1
//
//	The following 'ICUWard' object represents the current state of an ICU ward
//	in a hospital
let ICUWard = {
	name: "Sunset Mount General Hospital",
	room1: {
		capacity: generateRandomNumber(3, 4),
		patients: [
			{
				name: "Stella Allets",
				age: 43,
			},
			{
				name: "John Nnamchi",
				age: 24,
			},
			{
				name: "Gyn Erzo",
				age: 55,
			}
		]
	},
	room2: {
		capacity: generateRandomNumber(1, 2),
		patients: [
			{
				name: "Marl Carx",
				age: 90,
			}
		]
	}
}
// Your goal is to determine how many spots are left in the ICU ward
// saved into the 'spotsLeft' variable, and determine if the ward is at full
// capacity saved into the 'atFullCapacity' variable
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let spotsLeft = 0;
	for (let room in ICUWard) {
    if (room !== "name") {
        spotsLeft += ICUWard[room].capacity - ICUWard[room].patients.length;
    }
}
let atFullCapacity = (spotsLeft === 0)

////////////////////////////////////////////////////////////////////////



///////////////////////////////////////////////////////////////////////
//
//	EXERCISE 10 - DEEP OBJECT 2
//
//	The following 'solarSystem' object represents a simplified version of
//	our solar system. Distances and sizes are in Km.
let solarSystem =	{
	name: "Solar System",
	properties: {
		size: 18200000000,
		location: {
			x: 3284,
			y: -223,
			z: 43910
		},
		planets: [
			{
				name: "Mercury",
				distance: 47000000,
				atmosphere: {}
			},
			{
				name: "Venus",
				distance: 108000000,
				atmosphere: {
					carbonDioxide: 96,
					other: 4
				}
			},
			{
				name: "Earth",
				distance: 150000000,
				atmosphere: {
					nitrogen: 75,
					oxygen: generateRandomNumber(19, 22),
					argon: generateRandomNumber(1, 2),
					other: 1,
				}
			},
			{
				name: "Mars",
				distance: 215000000,
				atmosphere: {
					carbonDioxide: 95,
					nitrogen: 3,
					argon: generateRandomNumber(1, 2),
					other: 1,
				}
			}
		]
	}
}
// Complete each of the following tasks:
// - Calculate the solar system's distance from origin using the x, y and z
//	 coordinates, saved into 'distanceFromOrigin' rounded to nearest INTEGER
// - Calculate the size of the solar system in astronomical units saved
//	 into 'sizeInAUs' to 2 decimal places - a STRING will be allowed here
// - Determine if both Earth and Mars have the same amount of argon saved
//	 into 'argonOnEarthLikeMars'
// - This solar system is incomplete, append the Jupiter object 'jupiter' to the
//	 list of planets
let jupiter = {
	name: "Jupiter",
	distance: 775000000,
	atmosphere: {
		hydrogen: 90,
		helium: 10,
	}
}
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let distanceFromOrigin = Math.round(
    Math.sqrt(
        solarSystem.properties.location.x ** 2 +
        solarSystem.properties.location.y ** 2 +
        solarSystem.properties.location.z ** 2
    )
)

let sizeInAUs = (solarSystem.properties.size / 150000000).toFixed(2)
let argonOnEarthLikeMars = solarSystem.properties.planets[2].atmosphere.argon === solarSystem.properties.planets[3].atmosphere.argon
solarSystem.properties.planets.push(jupiter)

////////////////////////////////////////////////////////////////////////



/////////////////////// END OF OBJECTS EXERCISES ///////////////////////



////////////////////////////////////////////////////////////////////////
//
//															 ANSWERS
//
//	DO NOT LOOK AT THIS SECTION UNTIL YOU HAVE FINISHED THE EXERCISES
//
//	The following code tests the variables you need to work on to confirm your work is
//	correct. The if conditions check the variables are correct and the console.log()
//	statements are what make the print outs you see when you run the file. The below
//	is a crude demonstration of what we refer to as code tests. Code testing is a
//	common practice in the software engineer's role, where tests are run to confirm all
//	code runs correctly. Only when all tests pass would we give ourselves the green light
//	to ship code to production and feel confident the system will perform as expected.
//
////////////////////////////////////////////////////////////////////////

// setGreen instructs the shell to set the printed output to green
let setGreen = "\x1b[32m"
// setRed instructs the shell to set the printed output to red
let setRed = "\x1b[31m"
// resetColor instructs the shell to reset the printout color to standard
let resetColor = "\x1b[0m"
// tab adds a tab space for clarity on the array print outs
let tab = "		"

// Set correctMsg and incorrectMsg Messages so I don't need to write it everytimne
let correctMsg = setGreen + "Correct! " + resetColor
let incorrectMsg = setRed + "Incorrect! " + resetColor

// totalTests and passedTests count the final tally of passed tests
let totalTests = 0
let passedTests = 0

console.log("+----------------------------------+")
console.log("|                                  |")
console.log("|       EXERCISES START HERE       |")
console.log("|                                  |")
console.log("+----------------------------------+")
console.log()

// Object Initialization
let correctNewObject = {
	key: "value",
}
if (newObject !== undefined &&	newObject !== null && typeof newObject === 'object' && JSON.stringify(newObject) === JSON.stringify(correctNewObject)) {
	console.log(correctMsg + "The 'newObject' object you initialized looks like:")
	console.log(newObject)
	passedTests++
} else {
	console.log(incorrectMsg + "The initialized 'newObject' should be defined look like:")
	console.log(correctNewObject)
	console.log("but yours looks like:")
	console.log(newObject)
}
totalTests++
console.log()

// Add new key value pair
let correctAddNewKVPair = {
	one: 1,
	two: 2,
}
if (addNewKVPair !== undefined && JSON.stringify(addNewKVPair) === JSON.stringify(correctAddNewKVPair)) {
	console.log(correctMsg + "After adding a new KV pair to 'addNewKVPair' the object looks like:")
	console.log(addNewKVPair)
	passedTests++
} else {
	console.log(incorrectMsg + "After adding a new KV pair to 'addNewKVPair' the object should look like:")
	console.log(correctAddNewKVPair)
	console.log("but yours looks like:")
	console.log(addNewKVPair)
}
totalTests++
console.log()

// Get value of key
let correctPatientAge = getPatientAge.age
if (patientAge !== undefined && patientAge === correctPatientAge) {
	console.log(correctMsg + "The patient object looks like:")
	console.log(getPatientAge)
	console.log("and the 'patientAge' you got from it was: " + patientAge)
	passedTests++
} else {
	console.log(incorrectMsg + "The patient object looks like:")
	console.log(getPatientAge)
	console.log("and so 'patientAge' should be: " + correctPatientAge + ", but you got: " + patientAge)
}
totalTests++
console.log()

// Object Manipulation
patientCopy.age++
patientCopy.hobbies.shift()
patientCopy.pastConditions.push("vomiting")
if (patient !== undefined && JSON.stringify(patient) === JSON.stringify(patientCopy)) {
	console.log(correctMsg + "After manipulating 'patient' the object looks like:")
	console.log(patient)
	passedTests++
} else {
	console.log(incorrectMsg + "After manipulating 'patient' the object should look like:")
	console.log(patientCopy)
	console.log("but yours looks like:")
	console.log(patient)
}
totalTests++
console.log()

// Object contains key
let correctContains = 'hobbies' in checkContains
if (containsHobbies !== undefined && containsHobbies === correctContains) {
	console.log(correctMsg + "The 'checkContains' object looks like:")
	console.log(checkContains)
	console.log("and for if it contained the hobbies key in 'containsHobbies' you said it was: " + containsHobbies)
	passedTests++
} else {
	console.log(incorrectMsg + "The 'checkContains' object looks like:")
	console.log(checkContains)
	console.log("and for if it contained the hobbies key in 'containsHobbies', it should be: " + correctContains + ", but you got: " + containsHobbies)
}
totalTests++
console.log()

// Object sort keys
let correctSortedKeys = Object.keys(sortMyKeys).sort()
if (sortedKeys !== undefined && JSON.stringify(sortedKeys) === JSON.stringify(correctSortedKeys)) {
	console.log(correctMsg + "The keys of 'sortMyKeys' sorted into 'sortedKeys' array looks like:")
	console.log(sortedKeys)
	passedTests++
} else {
	console.log(incorrectMsg + "The keys of 'sortMyKeys' sorted into 'sortedKeys' array should look like:")
	console.log(correctSortedKeys)
	console.log("but it looks like:")
	console.log(sortedKeys)
}
totalTests++
console.log()

// Clear Object
if (JSON.stringify(clearMeCopy) === JSON.stringify({})) {
	console.log(correctMsg + "You cleared 'clearMe' properly and it looks like:")
	console.log(clearMe)
	console.log("and the other reference to it, 'clearMeCopy' was also cleared:")
	console.log(clearMeCopy)
	passedTests++
} else {
	console.log(incorrectMsg + "Both 'clearMe' and 'clearMeCopy' need to look like {}, 'clearMe' looks like:")
	console.log(clearMe)
	console.log("and the other reference to it, 'clearMeCopy' looks like:")
	console.log(clearMeCopy)
}
totalTests++
console.log()

// Object is empty
let correctIsEmpty = Object.keys(emptyObject).length < 1
if (isEmpty !== undefined && isEmpty === correctIsEmpty) {
	console.log(correctMsg + "The 'emptyObject' object looked like:")
	console.log(emptyObject)
	console.log("as to it being empty, you said this was: " + isEmpty)
	passedTests++
} else {
	console.log(incorrectMsg + "The 'emptyObject' object looked like:")
	console.log(emptyObject)
	console.log("as to it being empty, you said this was: " + isEmpty + ", but it should be " + correctIsEmpty)
}
totalTests++
console.log()

// Deep object 1
let correctSpotsLeft = (ICUWard.room1.capacity - ICUWard.room1.patients.length) + (ICUWard.room2.capacity - ICUWard.room2.patients.length)
let correctAtFullCapacity = correctSpotsLeft === 0
if (spotsLeft !== undefined && atFullCapacity !== undefined &&
	spotsLeft === correctSpotsLeft && atFullCapacity === correctAtFullCapacity) {
	console.log(correctMsg + "Room 1 and room 2's capacities were " + ICUWard.room1.capacity + " and " + ICUWard.room2.capacity + " respectively.")
	console.log("room 1 and room 2 had " + ICUWard.room1.patients.length + " and " + ICUWard.room2.patients.length + " patients respectively")
	console.log("hence the number of spots left saved in 'spotsLeft' was " + spotsLeft)
	console.log("and so as for the ICU being at full capacity, you said this was " + atFullCapacity)
	passedTests++
} else {
	console.log(incorrectMsg + "Room 1 and room 2's capacities were " + ICUWard.room1.capacity + " and " + ICUWard.room2.capacity + " respectively.")
	console.log("room 1 and room 2 had " + ICUWard.room1.patients.length + " and " + ICUWard.room2.patients.length + " patients respectively")
	console.log("hence the number of spots left saved in 'spotsLeft' should be " + correctSpotsLeft + " but you got " + spotsLeft)
	console.log("and so as for the ICU being at full capacity, this should be " + correctAtFullCapacity + " but you said this was " + atFullCapacity)
}
totalTests++
console.log()

// Deep object 2
let correctDistanceFromOrigin = Math.round(Math.sqrt(solarSystem.properties.location.x**2 + solarSystem.properties.location.y**2 + solarSystem.properties.location.z**2))
let correctSizeInAUs = (solarSystem.properties.size / solarSystem.properties.planets[2].distance).toFixed(2)
let correctArgonOnEarthLikeMars = solarSystem.properties.planets[2].atmosphere.argon === solarSystem.properties.planets[3].atmosphere.argon

if (distanceFromOrigin !== undefined && sizeInAUs !== undefined && argonOnEarthLikeMars !== undefined &&
	distanceFromOrigin === correctDistanceFromOrigin && sizeInAUs === correctSizeInAUs && argonOnEarthLikeMars === correctArgonOnEarthLikeMars &&
	solarSystem.properties.planets[4] !== undefined && solarSystem.properties.planets[4] === jupiter) {
	console.log(correctMsg + "All solar system tests passed!")
	console.log("- The solar system's distance from origin to nearest integer you got was: " + distanceFromOrigin)
	console.log("- The solar system's size in astronomical units to 2 decimal places you got was: " + sizeInAUs)
	console.log("- Earth's and Mars's argon compositions were: " + solarSystem.properties.planets[2].atmosphere.argon + "% and " +
	solarSystem.properties.planets[3].atmosphere.argon + "% respectively meaning them being equal you said was " + argonOnEarthLikeMars)
	console.log("- Finally, after adding Jupiter to the solar system's planets, the 5th element of the array looked like:")
	console.log(solarSystem.properties.planets[4])
	passedTests++
} else {
	console.log(incorrectMsg + "One or more solar system tests did not pass!")
	console.log("- The solar system's distance from origin to nearest integer should be " + correctDistanceFromOrigin + " but you got " + distanceFromOrigin)
	console.log("- The solar system's size in astronomical units to 2 decimal places should be " + correctSizeInAUs + " but you got " + sizeInAUs)
	console.log("- Earth's and Mars's argon compositions were: " + solarSystem.properties.planets[2].atmosphere.argon + "% and " +
	solarSystem.properties.planets[3].atmosphere.argon + "% respectively meaning them being equal should be " + correctArgonOnEarthLikeMars +
	" but you said this was " + argonOnEarthLikeMars)
	console.log("- Jupiter should now be added to the solar system's planets, and the 5th element of the array should look like:")
	console.log(jupiter)
	console.log("but it looks like:")
	console.log(solarSystem.properties.planets[4])
}
totalTests++
console.log()


// Final Test Tally Determination
if (passedTests === totalTests) {
	console.log(setGreen + "You passed " + passedTests + " / " + totalTests + " tests. Congratulations!" + resetColor)
} else {
	console.log(setRed + "You passed " + passedTests + " / " + totalTests + " tests. Keep Going!" + resetColor)
}



//////////////////////////// END OF ANSWERS ////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//													 HELPER FUNCTIONS
//
//	FEEL FREE TO LOOK AT THIS SECTION
//
//	The following code generates some variables that you need to check.
//	So you do not cheat, they generate them on a random basis that you
//	cannot predict. So you cannot and must perform the exercises the
//	right way. You can look at them though, they leverage conditionals
//	(if - else) to generate the values used in the tests, and we will
//	see conditionals in the 'Control Flows' chapter of this course
//
////////////////////////////////////////////////////////////////////////


// generateRandomNumber returns a random number between min and max (included)
// so that you cannot cheat and return literals based on the exercise setup
function generateRandomNumber(min, max) {
	return Math.floor(Math.random() * (max - min + 1) ) + min
}

// generateRandomObject returns a javascript object which may or may not have the
// hobbies key
function generateRandomObject() {
	let newObj = {
		name: "John Nnamchi",
		age: 23,
		pastConditions: [ "fever", "headache" ],
	}
	if (generateRandomNumber(0, 10) > 5) {
		newObj.hobbies = [ "soccer", "cooking" ]
	}
	return newObj
}

// generateRandomEmptyObject returns a javascript object which may or may not be empty
function generateRandomEmptyObject() {
	if (generateRandomNumber(0, 10) > 5) {
		return {}
	}
	let newObj = {
		name: "Not an empty object",
	}
	return newObj
}

// generateRandomConditions returns an array with a random number of values in it
function generateRandomConditions() {
	if (generateRandomNumber(0, 10) > 5) {
		return [ "fever", "headache" ]
	}
	return [ "fever", "headache", "coughing", "acne", "hair loss" ]
}