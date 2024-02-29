import axios from "axios";
import "./App.css";
import { useState, useEffect, useRef } from "react";

function App() {
  //set type useState
  const [type, setType] = useState("No Type to Display");
  //set random image useState
  const [randomPokemonImg, setRandomPokemonImg] = useState(null);
  //set the teammates useState
  const [teammates, setTeammates] = useState([]);
  const previousType = useRef("");

  //main function

  const getRandomPokemon = async () => {
    // useEffect(() => {
    try {
      setRandomPokemonImg(null);
      setTeammates([]);

      const randomPokemonId = Math.floor(Math.random() * 898) + 1;
      const response = await fetch(
        `https://pokeapi.co/api/v2/pokemon/${randomPokemonId}`
      );
      const data = await response.json();
      setRandomPokemonImg(data.sprites.front_default);
      if (previousType.current === data.types[0].type.name) {
        getRandomPokemon();
      }
      setType(data.types[0].type.name);
      // getPokemonTeam()
    } catch (error) {
      console.log(error.message);
    }
  };
  // Fetch teammates data
  const getPokemonTeam = async () => {
    try {
      const teammatesData = [];
      const responseTeammates = await fetch(
        `https://pokeapi.co/api/v2/type/${type}`
      );
      const typeData = await responseTeammates.json();
      const teammateNames = typeData.pokemon
        .slice(0, 5)
        .map((p) => p.pokemon.name);

      for (const teammateName of teammateNames) {
        const teammateSpriteUrl = await getPokemonSprite(teammateName);
        teammatesData.push(teammateSpriteUrl);
      }

      // Update teammates state after fetching all data
      setTeammates(teammatesData);
    } catch (error) {
      console.log(error.message);
    }
  };

  const getPokemonSprite = async (pokemon) => {
    try {
      const response = await fetch(
        `https://pokeapi.co/api/v2/pokemon/${pokemon}`
      );
      const data = await response.json();
      return data.sprites.front_default;
    } catch (error) {
      console.log(error.message);
      return null;
    }
  };

  useEffect(() => {
    getRandomPokemon();
  }, []);
  useEffect(() => {
    if (type != "No Type to Display") {
      getPokemonTeam();
    }
  }, [type]);

  return (
    <>
      <h1>Get A Random Pokemon</h1>
      <div className="card">
        <button onClick={getRandomPokemon}>Get Random Pokemon</button>
      </div>

      {randomPokemonImg && (
        <div className="pokemonTeamContainer">
          <p>{type ? type : "Type"}</p>
          <img
            src={randomPokemonImg ? randomPokemonImg : null}
            alt="Random Pokemon"
          />
        </div>
      )}

      <div className="pokemonTeamatesContainer">
        {teammates.map((teammateImg, index) => (
          <img key={index} src={teammateImg} alt={`Teammate ${index + 1}`} />
        ))}
      </div>
    </>
  );
}

export default App;
