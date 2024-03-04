function WordDisplay({ puzzleWord, guessedLetters }) {
  const puzzleWordArr = puzzleWord
    .split("")
    .map(letterInPuzzleWord => { 
        // console.log(letterInPuzzleWord);
        const isGuessed = guessedLetters[letterInPuzzleWord] || false;
        // console.log(isGuessed);

        return { val: letterInPuzzleWord, isGuessed }
    });

  // console.log('<WordDisplay/> puzzleWordArr', puzzleWordArr);

  const SPACE = " ";
  const renderLetter = (letter) => letter.isGuessed ? letter.val : SPACE;

  return (
    <>
      <div>
        {puzzleWordArr.map((letter, i) => (
          <span key={i}>{renderLetter(letter)}</span>
        ))}
      </div>
    </>
  );
}

export default WordDisplay;