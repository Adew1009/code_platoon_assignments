// import './App.css'
// import { useState } from 'react';




// function App() {
//   const[type, setType] = useState("No Type to Display");
//   const [randomPokemonImg, setRandomPokemonImg] = useState(null);
//   const [teammates, setTeammates] = useState([]);
//   const pokemonTeamatesContainer = document.getElementById('pokemonTeamates');

//   const getRandomPokemon = async () => {
//     try {
//       setRandomPokemonImg(null);
//       setTeammates([]);
//       let teammatesData = []
//       const randomPokemonId = Math.floor(Math.random() * 898) + 1;
//       let response = await fetch(`https://pokeapi.co/api/v2/pokemon/${randomPokemonId}`);
//       let data = await response.json()
//       //get image source
//       setRandomPokemonImg(data.sprites.front_default);
//       //get the type of pokemon
//       setType(data.types[0].type.name);
//       // console.log(type)
//       // console.log(randomPokemonImg)
//       pokemonTeamatesContainer.innerHTML = '';

//       //NOW TO WORK ON GETTING THE TEAM
//       let responseData = await fetch(`https://pokeapi.co/api/v2/type/${type}`);
//       let typeData = await responseData.json()
//       //get the list of pokemon of that type
//       //GET THE FIRST 5 pokemon of the random type
//       const teammateNames = typeData.pokemon.slice(0, 5).map(p => p.pokemon.name);

//       teammatesData = [];
//       for (const teammateName of teammateNames) {
//         const teammateSpriteUrl = await getPokemonSprite(teammateName);
//         teammatesData.push(teammateSpriteUrl);
//       }

//       setTeammates(teammates.concat(teammatesData));
//     } catch (error) {
//       console.log(error.message);
//     }
//   };

//   const getPokemonSprite = async (pokemon) => {
//     try {
//       const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`);
//       const data = await response.json();
//       return data.sprites.front_default;
//     } catch (error) {
//       console.log(error.message);
//       return null;
//     }
//   };
  

//   return (
//     <>
//       <body>
//         <h1>Get A Random Pokemon</h1>
//         <div className="card">
//           <button onClick={getRandomPokemon}>
//           Get Random Pokemon
//           </button>
//         </div>

//         <div className="pokemonTeamContainer" >
//           <p>{type ? type : "Type"}</p>
//           <img src={randomPokemonImg ? randomPokemonImg : null} alt="Random Pokemon" />
//         </div>

//         <div className="pokemonTeamatesContainer">
//           {teammates.map((teammateImg, index) => (
//             <img key={index} src={teammateImg} alt={`Teammate ${index + 1}`} />
//           ))}
//         </div>
//       </body >
//     </>
//   )
// }

// export default App
import './App.css';
import { useState } from 'react';

function App() {
  //set type useState
  const [type, setType] = useState("No Type to Display");
  //set random image useState
  const [randomPokemonImg, setRandomPokemonImg] = useState(null);
  //set the teammates useState
  const [teammates, setTeammates] = useState([]);


  //main function
  const getRandomPokemon = async () => {
    try {
      setRandomPokemonImg(null);
      setTeammates([]);
      const teammatesData = [];
      const randomPokemonId = Math.floor(Math.random() * 898) + 1;
      const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${randomPokemonId}`);
      const data = await response.json();
      setRandomPokemonImg(data.sprites.front_default);
      setType(data.types[0].type.name);

      // Fetch teammates data
      const responseTeammates = await fetch(`https://pokeapi.co/api/v2/type/${type}`);
      const typeData = await responseTeammates.json();
      const teammateNames = typeData.pokemon.slice(0, 5).map(p => p.pokemon.name);

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
      const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`);
      const data = await response.json();
      return data.sprites.front_default;
    } catch (error) {
      console.log(error.message);
      return null;
    }
  };

  return (
    <>
      <h1>Get A Random Pokemon</h1>
      <div className="card">
        <button onClick={getRandomPokemon}>Get Random Pokemon</button>
      </div>

      <div className="pokemonTeamContainer">
        <p>{type ? type : "Type"}</p>
        <img src={randomPokemonImg ? randomPokemonImg : null} alt="Random Pokemon" />
      </div>

      <div className="pokemonTeamatesContainer">
        {teammates.map((teammateImg, index) => (
          <img key={index} src={teammateImg} alt={`Teammate ${index + 1}`} />
        ))}
      </div>
    </>
  );
}

export default App;