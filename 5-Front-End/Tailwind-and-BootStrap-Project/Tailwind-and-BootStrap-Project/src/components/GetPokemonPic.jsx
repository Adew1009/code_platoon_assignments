import React, { useState, useEffect } from "react"; 
import axios from "axios"; 
import "../App.css";
import AllPokemonDropDownButton from "./AllPokemonDropDownButton";

const GetPokemonPic = (name) => {
  
  const [pokemonImg, setPokemonImg] = useState(null);

  useEffect(() => {
    const fetchPokemonImage = async () => {
      try {
        const response = await axios.get(
          `https://pokeapi.co/api/v2/pokemon/${name}`
        );
        const data = response.data;
        setPokemonImg(data.sprites.front_default);
      } catch (error) {
        console.log(error.message);
      }
    };
    fetchPokemonImage();
  }, [name]);

  return (
    <div>
      <img src={pokemonImg} alt="Pokemon" />
    </div>
  ); 
};

export default GetPokemonPic;
