exports.factorial = function(num) {
    // Using Recursion
    if (num === 0) {
        return 1;
    }
    return num * factorial(num - 1);
}
console.log(factorial(4));

exports.palindrome = function(string) {
    if (!string) {
        return true;
    } else if (string[0] !== string[string.length - 1]) {
        return false;
    }
    return palindrome(string.slice(1, -1));
};

exports.bottles = function(num) {
    function bottleLingo(numBottles) {
        if (numBottles > 1) {
            return `${numBottles} bottles`;
        }
        return `${numBottles} bottle`;
    }
    if (num === 1) {
        console.log(`${bottleLingo(num)} of beer on the wall, ${bottleLingo(num)} of beer. Take one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.`);
    }
    if (num > 1) {
        const mainString = `${bottleLingo(num)} of beer on the wall, ${bottleLingo(num)} of beer. Take one down and pass it around, ${bottleLingo(num - 1)} of beer on the wall.`;
        console.log(mainString);
        bottles(num - 1);
    }
};

exports.romanNum = function (num, index = 0, output = "") {
    const romanNumeral = [
        ["M", 1000], ["CM", 900], ["D", 500], ["C", 100], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1],
        ["M", 1000], ["CM", 900], ["D", 500], ["C", 100], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]
    ];
    if (index >= romanNumeral.length) {
        return output;
    }
    const value = romanNumeral[index][1];
    const numeral = romanNumeral[index][0];
    if (num >= value) {
        const timesOfNumeral = Math.floor(num / value);
        output += numeral.repeat(timesOfNumeral);
        num %= value;
    }
    return romanNum(num, index + 1, output);
}

console.log(romanNum(944));
;
