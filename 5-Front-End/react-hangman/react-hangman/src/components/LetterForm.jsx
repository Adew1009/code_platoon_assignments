import { useState } from "react";
function LetterForm({ handleGuess }) {
  const [inputField, setInputField] = useState("");

  const handleClick = () => {
    console.log("guess letter click");
    handleGuess(inputField);
  };

  return (
    <>
      <h2>Letterform</h2>
      <input
        value={inputField}
        onChange={(e) => setInputField(e.target.value)}
        placeholder="Letter to guess"
      ></input>
      <button onClick={handleClick}>Guess this letter!</button>
    </>
  );
}

export default LetterForm;
