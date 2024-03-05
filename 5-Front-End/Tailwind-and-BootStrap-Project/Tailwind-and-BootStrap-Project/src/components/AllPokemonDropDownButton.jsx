import allPokemonName from './AllPokemonName.jsx';
import { useEffect, useState } from 'react';
import ButtonGroup from "react-bootstrap/ButtonGroup";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";


function AllPokemonDropDownButton(props) {
 const [pokemonNames, setPokemonNames] = useState([])    
//  useEffect(bodyofafunction, dependancylist) 
useEffect(()=>{
  const setPokemon = async () => {setPokemonNames( await allPokemonName())}
  setPokemon()
}, [])
// useEffect(()=>{console.log(pokemonNames)}, [pokemonNames])
    // const handlePokemonClick = (e,pokemonName) => {
    //   // console.log(e)
    //   // console.log(pokemonName)
    //   GetPokemonPic(pokemonName); // Corrected function call
    // };


  return (
    <DropdownButton
      // id="dropdown-item-button"
      id="dropdown-variants-Warning"
      title="Pokemon Dropdown button"
      data-bs-theme="dark"
      variant="warning"
    >
      {pokemonNames.map((pokemonName) => (
        <Dropdown.Item
          onClick={(e) => {
            props.handlePokemonClick(e, pokemonName);
          }}
          
          as="button"
          id={pokemonName}
          key={pokemonName}
        >
          {" "}
          {pokemonName}{" "}
        </Dropdown.Item>
      ))}
    </DropdownButton>
  );
}

export default AllPokemonDropDownButton;

