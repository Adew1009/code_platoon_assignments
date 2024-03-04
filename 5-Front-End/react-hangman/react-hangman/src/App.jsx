import { useState } from "react";
import "./App.css";
import words from "./data/words.json";
import WordDisplay from "./components/WordDisplay";
import BadGuessDisplay from "./components/BadGuessDisplay";
import LetterForm from "./components/LetterForm";

function App() {
  // console.log(words);

  // Fake data we can use to make our dev workflow easier and faster



  // Get a random word to guess from an array of possible words.
  const getPuzzleWord = (possibleWords) => {
    const index = Math.floor(Math.random() * possibleWords.length);
    return possibleWords[index];
  };


  // Create state for our word to guess - the `puzzleWord`
  const [puzzleWord, setPuzzleWord] = useState(getPuzzleWord(words));
  // Create state which will hold an obj we'll use as a dict to track guessed letters
  // and which guesses were correct.
  const initialGuessedLetters = {};
  const [guessedLetters, setGuessedLetters] = useState(initialGuessedLetters)

  const handleGuess = (letter) => {
    console.log("handleguess ", letter);
    // Letter already guessed
    if (letter in guessedLetters) {
      alert("Letter already guessed!");

      // New guess
    } else {
      const updated = { ...guessedLetters };
      console.log("updated", updated);

      if (puzzleWord.includes(letter)) {
        updated[letter] = true;
      } else {
        updated[letter] = false;
      }

      setGuessedLetters(updated);
    }
  };

  const NUM_ALLOWED_GUESSES = 6;

  function getBadLetters() {
    const letters = Object.keys(guessedLetters);
    return letters.filter((l) => !guessedLetters[l]);
  }

  function calculateNumGuessesLeft() {
    const numBadGuesses = getBadLetters().length;
    return NUM_ALLOWED_GUESSES - numBadGuesses;
  }

  console.log("guesses left ", calculateNumGuessesLeft());

  const renderWinMessage = () => {
    const lettersLeftToGuess = puzzleWord.split("").filter((l) => {
      console.log(l);
      // If a letter in the word has been guessed correctly
      if (guessedLetters[l] === true) {
        console.log("guessed right");
        return false;
      }
      console.log("not guessed yet");
      return true;
    });

    if (lettersLeftToGuess.length === 0) {
      return <h2>You Won!</h2>;
    }

    return null;
  };

  const renderLoseMessage = () => {
    if (calculateNumGuessesLeft() === 0) {
      return <h2>You Lost!</h2>;
    }

    return null;
  };

  return (
    <>
      <h1>React Hangman</h1>
      {renderWinMessage()}
      {renderLoseMessage()}
      <p>{puzzleWord}</p>
      <WordDisplay puzzleWord={puzzleWord} guessedLetters={guessedLetters} />
      <BadGuessDisplay guessedLetters={guessedLetters} />
      <LetterForm handleGuess={handleGuess} />
    </>
  );
}

export default App;
