function toRomanLazy(num) {
  let total = num
  let output = "";

  const romanNumeralToArabic = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
  }
  const romanNumeralPriorityOrder = ["M", "D", "C", "L", "X", "V", "I"]
  // console.log(romanNumeralToArabic['X'])

  for (let i = 0; i < romanNumeralPriorityOrder.length; i++) {
    const valueOfNumeral = romanNumeralToArabic[romanNumeralPriorityOrder[i]]
    const numOfNumerals = Math.floor(total / valueOfNumeral)

    // console.log("numOfNumerals ",romanNumeralPriorityOrder[i],": " , numOfNumerals)

    if (numOfNumerals > 0) {
      const valueOfNON = numOfNumerals * valueOfNumeral
      total = total - valueOfNON

      for (j = 0; j < numOfNumerals; j++) {
        output += romanNumeralPriorityOrder[i]
      }
    }
  }
  return (output)
}

function toRoman(num) {
  let total = num
  let output = "";

  const romanNumeralToArabic = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
  }
  const romanNumeralPriorityOrder = ["M", "CM", "D", "CD", "C", "L", "XL", "X", "IX", "V", "IV", "I"]
  // console.log(romanNumeralToArabic['X'])

  for (let i = 0; i < romanNumeralPriorityOrder.length; i++) {
    const valueOfNumeral = romanNumeralToArabic[romanNumeralPriorityOrder[i]]
    const numOfNumerals = Math.floor(total / valueOfNumeral)

    // console.log("numOfNumerals ",romanNumeralPriorityOrder[i],": " , numOfNumerals)

    if (numOfNumerals > 0) {
      const valueOfNON = numOfNumerals * valueOfNumeral
      total = total - valueOfNON

      for (j = 0; j < numOfNumerals; j++) {
        output += romanNumeralPriorityOrder[i]
      }
    }
  }
  return (output)
}
console.log(toRoman(4))

module.exports = { toRoman, toRomanLazy };

