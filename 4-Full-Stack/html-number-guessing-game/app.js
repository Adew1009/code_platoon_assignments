let randomNumber=(Math.floor(Math.random() * 100))+1

console.log(`HELLO WHISKEY PLATOON! Your secret number is ${randomNumber}.`)

const addGuess = (event) => {
    event.preventDefault()
    let guessedNums= document.getElementById('guessedNums')
    let guessedNum = document.getElementById('Guess').value;
    let li = document.createElement('li')
    li.innerText = `Guess: ${guessedNum}`
    guessedNums.appendChild(li)
    higOrLow(guessedNum)
    document.getElementById('Guess').value="";

}
const higOrLow = (num) => {
    if (num>randomNumber) {
        highOrLow.textContent = "Your Guess is too high!"
    } else if (num < randomNumber) {
        highOrLow.textContent = "Your Guess is too Low!"
    } else if (num == randomNumber) {
        highOrLow.textContent = `You Guessed the correct number of ${randomNumber}!`
        document.getElementById("highOrLow").style.backgroundColor= "Green";
        document.getElementById("highOrLow").style= "color: black; font-size: 80px; font-weight: 600; background: green"
        document.getElementById('Guess').placeholder  = 'YOU DID IT!'
        document.getElementById('page').style.backgroundColor = "yellow"
        document.getElementById("title").innerText = "!!!!!!YOU WON!!!!!"
        document.getElementById("title").style = "color: black; font-size: 80px; font-weight: 600;background: green" 
        document.getElementById("form").innerHTML = ""
        document.getElementById("guessedNums").innerHTML = ""
    }
}