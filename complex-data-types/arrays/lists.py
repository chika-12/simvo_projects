////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 1 - INITALIZATION
//
//	Initialize the 'newArray' variable as any kind of non-empty array
//	literal with at least one element in it
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let newArray = ["blue", "green", "red"]

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 2 - IS ARRAY
//
//	Check if 'maybeAnArray' is an array and save the result into 'isAnArray'
let maybeAnArray = generateRandomDataType()
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let isAnArray = Array.isArray(maybeAnArray)

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 3 - ARRAY REFERENCES
//
//	We have the variable 'array1':
let array1 = [ "Just", "your", "average", "array" ]
//	And 'array2' that is assigned the reference of 'array1'
let array2 = array1
//	And 'array3' that is assigned a deep copy of 'array1'
let array3 = JSON.parse(JSON.stringify(array1))
//	Tasks:
//	- Change the value of the first element of 'array2' from "Just" to "Not"
//	- Change the value of the last element of 'array3' from "array" to "copy"
//	- They will all be printed out in the answers, and you will see how assigning
//		them by reference vs making a copy of an array affects each variable's output
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////
array2[0] = "Not"
array3[3] = "copy"


////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 4 - ARRAY UNSHIFT AND PUSH
//
//	Add the element "zero" to the begining of the 'growMe' array and add
//	the element "three" to the end of the 'growMe' array
let growMe = [ "one", "two" ]
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////
growMe.unshift("zero")
growMe.push("three")


////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 5 - ARRAY SHIFT AND POP
//
//	Remove the first and last item of the 'shrinkMe' array
let shrinkMe = [ 1, 2, 3, 4 ]
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////
shrinkMe.shift("1")
shrinkMe.pop("3")

////////////////////////////////////////////////////////////////////////

 

////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 6 - ARRAY CONCAT
//
//	Concatenate arrays 'marysList' and 'johnsList' and save the result
//	into 'mergedLists'
let marysList = [ "Apple", "Banana", "Cherry", "Durian" ]
let johnsList = [ "Elderberry", "Fig", "Guava" ]
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let mergedLists = marysList.concat(johnsList)

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 7 - ARRAY LENGTH
//
//	Get the number of elements in 'getMyLength' and save the result into
//	arrayLength
let getMyLength = generateRandomLengthArray()
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let arrayLength = getMyLength.length

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 8 - GET ELEMENT AT INDEX
//
//	Get the 'nthElement' element of 'getMyNthElement' and save the result into
//	'arrayNthElement'
let getMyNthElement = [ "How", "many", "elements", "do", "I", "have", "?" ]
let nthElement = generateRandomNumber(1, getMyNthElement.length)
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let arrayNthElement = getMyNthElement[nthElement - 1]

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 9 - ARRAY SLICE
//
//	Choosing the correct start and end indices, get a slice of 'getMySlice'
//	and save the result into 'arraySlice' so that 'arraySlice' becomes:
//	[ "wood", "would", "a", "woodchuck" ]
let getMySlice = [ "How", "much", "wood", "would", "a", "woodchuck", "chuck", "?" ]
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let arraySlice = getMySlice.slice(2, 6)

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 10 - ARRAY INSERT
//
//	Insert multiple elements into the 'insertIntoMe' so that it looks like:
//	[ "Well", "that", "was", "easy", "!" ]
//	Hint: Function is called splice()
let insertIntoMe = [ "Well", "easy", "!" ]
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////
insertIntoMe.splice(1, 0, "that", "was")


////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 11 - ARRAY REMOVE
//
//	Delete multiple elements from the 'removeFromMe' array so that it looks like:
//	[ "You", "know", "sometimes", "less", "is", "more" ]
//	Hint: You should use the same function as array insert
let removeFromMe = [ "You", "know", "what", "they", "say", "sometimes", "less", "is", "more" ]
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

removeFromMe.splice(2, 3)

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 12 - ARRAY INCLUDES
//
//	Check if the 'breakfastList' array includes "bacon" and save the result
//	into 'breakfastIncludesBacon'
let breakfastList = generateRandomBreakfastList()
//	 NOTE: 'breakfastIncludesBacon' should be a boolean value of True or False
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let breakfastIncludesBacon = breakfastList.includes("bacon")

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 13 - ARRAY SORT ASCENDING
//
//	Sort the following 'sortMe' array in alphabetical order
let sortMe = generateGroceryList()
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////
sortMe.sort()


////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 14 - ARRAY SORT DESCENDING
//
//	Sort the following 'sortAndReverseMe', then reverse it, so that the
//	strings are sorted in descending order
let sortAndReverseMe = generateGroceryList()
//	NOTE: Remember the dot notation expression1().expression2() turns the output
//	of expression1 into the input of expression2
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

sortAndReverseMe.sort().reverse()

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 15 - SPLIT STRING INTO AN ARRAY
//
//	Split the following 'splitMeIntoArray' string into an array, using the
//	correct delimiter so that the array only contains the words of the sentence
//	with no spaces, and save the result into 'arrayFromSplitString'
let splitMeIntoArray = "The quick brown fox jumps over the lazy dog"
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let arrayFromSplitString = splitMeIntoArray.split(" ")

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 16 - JOIN ARRAY INTO A STRING
//
//	Join the following 'joinMeIntoString' array into a string, using the
//	correct delimiter so that the string represents a valid IP Address
//	and save the result into 'stringFromJoinedArray'
let joinMeIntoString = [ 106, 162, 9, 2 ]
//	NOTE: Example of valid IP Address: "10.9.123.9"
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let stringFromJoinedArray = joinMeIntoString.join(".")

////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////
//
//	EXERCISE 17 - ARRAY TIC TAC TOE
//
//	An array can contain an array as its elements, such an array is called
//	a 2-Dimensional array. The variable 'ticTacToeArray' is a 2-Dimensional array
//	that reflects a tic tac toe game state:
let ticTacToeArray = generateRandomTicTacToe()
//	The 2-D Array returned here is EXACTLY how tic tac toe games online are programmed.
//
//	Your objective is to determine if a player has won the game through this
//	winning diagonal pattern:
//	| * |	 |	 |
//	|---|---|---|
//	|	 | * |	 |
//	|---|---|---|
//	|	 |	 | * |
//
//	Write a boolean expression checking that ALL THREE OF THESE CELLS contain
//	the same character and save the result into 'ticTacToeWinner'. "O" is
//	used for the noughts player and "X" is used for the crosses player - but
//	you don't really need that information.
//
////////////////////// YOUR CODE BELOW THIS LINE ///////////////////////

let ticTacToeWinner = ticTacToeArray[0][0] !== "" && ticTacToeArray[0][0] === ticTacToeArray[1][1] && ticTacToeArray[1][1] === ticTacToeArray[2][2]

////////////////////////////////////////////////////////////////////////



//////////////////////// END OF ARRAY EXERCISES ////////////////////////



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

// Array Initialization
if (newArray !== undefined && newArray.length > 0 && Array.isArray(newArray)) {
	console.log(correctMsg + "The 'newArray' array you initialized looks like: ")
	console.log(newArray)
	passedTests++
} else {
	console.log(incorrectMsg + "The initialized 'newArray' should be defined and have a length of more than 0, but yours looks like " + newArray)
}
totalTests++
console.log()

// Is Array
let correctIsArray = Array.isArray(maybeAnArray)
if (isAnArray !== undefined && isAnArray === correctIsArray) {
	console.log(correctMsg + "As for the variable 'maybeAnArray' being an array, you found this was " + isAnArray)
	passedTests++
} else {
	console.log(incorrectMsg + "As for the variable 'maybeAnArray' being an array, this should be " + correctIsArray + " but you got " + isAnArray)
}
totalTests++
console.log()

// Array references
let correctArray1n2 = [ "Not", "your", "average", "array" ]
let correctArray3 = [ "Just", "your", "average", "copy" ]
if (JSON.stringify(array1) === JSON.stringify(correctArray1n2) &&
		JSON.stringify(array2) === JSON.stringify(correctArray1n2) &&
		JSON.stringify(array3) === JSON.stringify(correctArray3)) {
	console.log(correctMsg + "The references exercises yielded the following")
	console.log("'array1' looks like:")
	console.log(array1)
	console.log("'array2' looks like:")
	console.log(array2)
	console.log("Notice how 'array1' and 'array2' are identical as they were assigned BY REFERENCE")
	console.log("Meanwhile 'array3' looks like:")
	console.log(array3)
	console.log("Notice how it is its own array reference as it was assigned a DEEP COPY of 'array1'")
	passedTests++
} else {
	console.log(incorrectMsg + "The references exercises yielded the following")
	console.log("'array1' looks like:")
	console.log(array1)
	console.log("'array2' looks like:")
	console.log(array2)
	console.log("But they should look like")
	console.log(correctArray1n2)
	console.log("Meanwhile 'array3' looks like:")
	console.log(array3)
	console.log("But it should look like:")
	console.log(correctArray3)
}
totalTests++
console.log()

// Array Push
let correctGrowArray = [ "one", "two" ]
correctGrowArray.unshift("zero")
correctGrowArray.push("three")
if (growMe !== undefined && JSON.stringify(growMe) === JSON.stringify(correctGrowArray)) {
	console.log(correctMsg + "After adding \"zero\" to the beginning and \"three\" to the end of 'growMe', 'growMe' is:")
	console.log(growMe)
	passedTests++
} else {
	console.log(incorrectMsg + "After adding \"zero\" to the beginning and \"three\" to the end of 'growMe', 'growMe' should be:")
	console.log(correctGrowArray)
	console.log("but you got:")
	console.log(growMe)
}
totalTests++
console.log()

// Array Shift
let correctShrinkArray = [ 1, 2, 3, 4 ]
correctShrinkArray.shift()
correctShrinkArray.pop()
if (shrinkMe !== undefined && JSON.stringify(shrinkMe) === JSON.stringify(correctShrinkArray)) {
	console.log(correctMsg + "After removing the first and last elements of 'shrinkMe', 'shrinkMe' is:")
	console.log(shrinkMe)
	passedTests++
} else {
	console.log(incorrectMsg + "After removing the first and last elements of 'shrinkMe', 'shrinkMe' should be:")
	console.log(correctShrinkArray)
	console.log("but you got:")
	console.log(shrinkMe)
}
totalTests++
console.log()

// Array Concat
let correctMergedList = marysList.concat(johnsList)
if (mergedLists !== undefined && JSON.stringify(mergedLists) === JSON.stringify(correctMergedList)) {
	console.log(correctMsg + "After concatenating 'marysList' and 'johnsList', 'mergedLists' is:")
	console.log(mergedLists)
	passedTests++
} else {
	console.log(incorrectMsg + "After concatenating 'marysList' and 'johnsList', 'mergedLists' should be:")
	console.log(correctMergedList)
	console.log("but you got:")
	console.log(mergedLists)
}
totalTests++
console.log()

// Array Length
let correctArrayLength = getMyLength.length
if (arrayLength !== undefined && arrayLength === correctArrayLength) {
	console.log(correctMsg + "The 'getMyLength' array looked like:")
	console.log(getMyLength)
	console.log("And number of elements in the 'getMyLength' array you got was: " + arrayLength)
	passedTests++
} else {
	console.log(incorrectMsg + "The 'getMyLength' array looked like:")
	console.log(getMyLength)
	console.log("And the number of elements in the 'getMyLength' array should be " + correctArrayLength + " but you got " + arrayLength)
}
totalTests++
console.log()

// Array Get Nth Element
let correctNthElement = getMyNthElement[nthElement-1]
if (arrayNthElement !== undefined && arrayNthElement === correctNthElement) {
	console.log(correctMsg + "The 'getMyNthElement' array looked like:")
	console.log(getMyNthElement)
	console.log("Element number " + nthElement + " in the 'getMyNthElement' array you got was: '" + arrayNthElement + "'")
	passedTests++
} else {
	console.log(incorrectMsg + "The 'getMyNthElement' array looked like:")
	console.log(getMyNthElement)
	console.log("Element number " + nthElement + " in the 'getMyNthElement' array should be '" + correctNthElement + "' but you got '" + arrayNthElement + "'")
}
totalTests++
console.log()

// Array Slice
let correctArraySlice = getMySlice.slice(2, 6)
if (arraySlice !== undefined && JSON.stringify(arraySlice) === JSON.stringify(correctArraySlice)) {
	console.log(correctMsg + "The slice of 'getMySlice' you got was:")
	console.log(arraySlice)
	passedTests++
} else {
	console.log(incorrectMsg + "The slice of 'getMySlice' should be:")
	console.log(correctArraySlice)
	console.log("but you got:")
	console.log(arraySlice)
}
totalTests++
console.log()

// Array Insert
let correctInsertedArray = [ "Well", "easy", "!" ]
correctInsertedArray.splice(1, 0, "that", "was")
if (insertIntoMe !== undefined && JSON.stringify(insertIntoMe) === JSON.stringify(correctInsertedArray)) {
	console.log(correctMsg + "After inserting \"that\" and \"was\" elements into of 'insertIntoMe', 'insertIntoMe' looks like:")
	console.log(insertIntoMe)
	passedTests++
} else {
	console.log(incorrectMsg + "After inserting \"that\" and \"was\" elements into of 'insertIntoMe', 'insertIntoMe' should be:")
	console.log(correctInsertedArray)
	console.log("but you got:")
	console.log(insertIntoMe)
}
totalTests++
console.log()

// Array Remove
let correctRemovedArray = [ "You", "know", "what", "they", "say", "sometimes", "less", "is", "more" ]
correctRemovedArray.splice(2, 3)
if (removeFromMe !== undefined && JSON.stringify(removeFromMe) === JSON.stringify(correctRemovedArray)) {
	console.log(correctMsg + "After deleting elements from 'removeFromMe', 'removeFromMe' looks like:")
	console.log(removeFromMe)
	passedTests++
} else {
	console.log(incorrectMsg + "After deleting elements from 'removeFromMe', 'removeFromMe' should be:")
	console.log(correctRemovedArray)
	console.log("but you got:")
	console.log(removeFromMe)
}
totalTests++
console.log()

// Array Includes
let correctBreakfastIncludesBacon = breakfastList.includes("bacon")
if (breakfastIncludesBacon !== undefined && breakfastIncludesBacon === correctBreakfastIncludesBacon) {
	console.log(correctMsg + "As for the variable 'breakfastList' including \"bacon\", you found this was " + breakfastIncludesBacon)
	passedTests++
} else {
	console.log(incorrectMsg + "As for the variable 'breakfastList' including \"bacon\", this should be " + correctBreakfastIncludesBacon + " but you got " + breakfastIncludesBacon)
}
totalTests++
console.log()

// Array Sort
let sortMeCopy = [ "Cherry", "Elderberry", "Fig", "Apple", "Durian", "Guava", "Banana" ]
sortMeCopy.sort()
if (sortMe !== undefined && JSON.stringify(sortMe) === JSON.stringify(sortMeCopy)) {
	console.log(correctMsg + "After sorting the elements in 'sortMe', 'sortMe' looks like:")
	console.log(sortMe)
	passedTests++
} else {
	console.log(incorrectMsg + "After sorting the elements in 'sortMe', 'sortMe' should be:")
	console.log(sortMeCopy)
	console.log("but you got:")
	console.log(sortMe)
}
totalTests++
console.log()

// Sort And Reverse
let sortAndReverseMeCopy = [ "Cherry", "Elderberry", "Fig", "Apple", "Durian", "Guava", "Banana" ]
sortAndReverseMeCopy.sort().reverse()
if (sortAndReverseMe !== undefined && JSON.stringify(sortAndReverseMe) === JSON.stringify(sortAndReverseMeCopy)) {
	console.log(correctMsg + "After sorting and reversing the elements in 'sortAndReverseMe', 'sortAndReverseMe' looks like:")
	console.log(sortAndReverseMe)
	passedTests++
} else {
	console.log(incorrectMsg + "After sorting and reversing the elements in 'sortAndReverseMe', 'sortAndReverseMe' should be:")
	console.log(sortAndReverseMeCopy)
	console.log("but you got:")
	console.log(sortAndReverseMe)
}
totalTests++
console.log()

// Split String Into Array
let correctArrayFromSplitString = splitMeIntoArray.split(" ")
if (arrayFromSplitString !== undefined && JSON.stringify(arrayFromSplitString) === JSON.stringify(correctArrayFromSplitString)) {
	console.log(correctMsg + "After splitting string 'splitMeIntoArray' into the array 'arrayFromSplitString', 'arrayFromSplitString' looks like:")
	console.log(arrayFromSplitString)
	passedTests++
} else {
	console.log(incorrectMsg + "After splitting string 'splitMeIntoArray' into the array 'arrayFromSplitString', 'arrayFromSplitString' should be:")
	console.log(correctArrayFromSplitString)
	console.log("but you got:")
	console.log(arrayFromSplitString)
}
totalTests++
console.log()

// Join Array Into String
let correctStringFromJoinArray = joinMeIntoString.join(".")
if (stringFromJoinedArray !== undefined && JSON.stringify(stringFromJoinedArray) === JSON.stringify(correctStringFromJoinArray)) {
	console.log(correctMsg + "After joining array 'joinMeIntoString' into the string 'stringFromJoinedArray', 'stringFromJoinedArray' looks like:")
	console.log(stringFromJoinedArray)
	passedTests++
} else {
	console.log(incorrectMsg + "After joining array 'joinMeIntoString' into the string 'stringFromJoinedArray', 'stringFromJoinedArray' should be:")
	console.log(correctStringFromJoinArray)
	console.log("but you got:")
	console.log(stringFromJoinedArray)
}
totalTests++
console.log()

// Array Tic Tac Toc
let correctTicTacToeWinner = ticTacToeArray[0][0] === ticTacToeArray[1][1] && ticTacToeArray[0][0] === ticTacToeArray[2][2] && ticTacToeArray[0][0] !== ""
if (ticTacToeWinner !== undefined && ticTacToeWinner === correctTicTacToeWinner) {
	console.log(correctMsg + "The tic tac toe game array looks like:")
	console.log("[")
	console.log(ticTacToeArray[0])
	console.log(ticTacToeArray[1])
	console.log(ticTacToeArray[2])
	console.log("]")
	console.log("And you said there being a diagonal winner was " + ticTacToeWinner)
	passedTests++
} else {
	console.log(incorrectMsg + "The tic tac toe game array looks like:")
	console.log("[")
	console.log(ticTacToeArray[0])
	console.log(ticTacToeArray[1])
	console.log(ticTacToeArray[2])
	console.log("]")
	console.log("And there being a diagonal winner should be " + correctTicTacToeWinner + " but you said " + ticTacToeWinner)
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
// so that you cannot cheat and write boolean literals based on the exercise setup
function generateRandomNumber(min, max) {
	return Math.floor(Math.random() * (max - min + 1) ) + min
}

// generateRandomDataType returns either a string or array randomly
function generateRandomDataType() {
	if (generateRandomNumber(0, 10) > 5) {
		return [ "this", "is", "an", "array"]
	}
	return "This is not an array"
}

// generateRandomLengthArray randomizes a number and returns an array of
// that length
function generateRandomLengthArray() {
	let length = generateRandomNumber(3, 7)
	let newArray = [ "The", "numbers", ]
	for (let i = 0; i < length; i++) {
		newArray.push(generateRandomNumber(10, 100).toString())
	}
	newArray.push("are", "lucky")
	return newArray
}

// generateRandomBreakfastList returns an array with either bacon included in it
// or not
function generateRandomBreakfastList() {
	if (generateRandomNumber(0, 10) > 5) {
		return [ "milk", "eggs", "bacon", "orange juice" ]
	}
	return [ "milk", "eggs", "orange juice" ]
}

// generateGroceryList returns a standard list of strings
function generateGroceryList() {
	return [ "Cherry", "Elderberry", "Fig", "Apple", "Durian", "Guava", "Banana" ]
}

// generateRandomTicTacToe returns one of three possible states of a tic tac toe
// game randomly, one of them having the X player win with a diagonal line, and
// other two with neither player winning
function generateRandomTicTacToe() {
	if (generateRandomNumber(0, 10) > 5) {
		if (generateRandomNumber(0, 10) > 5) {
			return [
				[ "X", "O", "X" ],
				[ "", "O", "O" ],
				[ "", "", "X" ]
			]
		}
		return [
			[ "", "X", "O" ],
			[ "X", "", "X" ],
			[ "O", "O", "" ]
		]
	}
	return [
		[ "X", "O", "O" ],
		[ "", "X", "O" ],
		[ "", "", "X" ]
	]
}