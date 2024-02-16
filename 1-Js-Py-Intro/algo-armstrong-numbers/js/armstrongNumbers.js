// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(listOfNumbers) {

function createArrayOfNum(maxValue) {
    return [...Array(maxValue).keys()];
}


function numberToPower(digit, power){
    return digit**power
}


// function findArmstrongNumbers(listOfNumbers) {
let answerArray = []

for (i=0; i<listOfNumbers.length; i++){
    const individualNumber = listOfNumbers[i]
    const individualNumberString = individualNumber.toString()
    const digitsInIndividualNumber = individualNumberString.length
    let sumOfDigitsToPower = 0

    for (j=0; j<digitsInIndividualNumber; j++){
        const eachDigit = individualNumberString[j]
        const digitToPower = numberToPower(eachDigit, digitsInIndividualNumber)
        sumOfDigitsToPower += digitToPower
    }
    if (sumOfDigitsToPower==individualNumber){
        answerArray.push(individualNumber)
        
    }
    sumOfDigitsToPower = 0
}
return answerArray
}
// }
