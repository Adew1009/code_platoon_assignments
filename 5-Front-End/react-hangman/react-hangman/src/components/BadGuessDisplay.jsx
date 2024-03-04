function BadGuessDisplay({ guessedLetters }) {
  const letters = Object.keys(guessedLetters);

  const badLetters = letters.filter((l) => !guessedLetters[l]);
  const numBadGuesses = badLetters.length;
  const numAllowedGuesses = 6;

  //   console.log(numBadGuesses);
  //   console.log(numAllowedGuesses)

  return (
    <>
      <h2>Bad Guesses</h2>
      <div>
        {badLetters.map((l, i) => (
          <span key={i}>{l}</span>
        ))}
      </div>
      <h3>{numAllowedGuesses - numBadGuesses} Guesses Left</h3>
    </>
  );
}

export default BadGuessDisplay;
