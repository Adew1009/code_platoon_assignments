import axios from 'axios';

const allPokemonName = async () => {
  try {
    const response = await axios.get(
      `https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0`
    );
    const data = response.data;
    const allNames= data.results.map(pokemon => pokemon.name)
    return allNames
  } catch (error) {
    console.log(error.message);
  }
};

export default allPokemonName
