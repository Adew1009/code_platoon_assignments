const getButton = document.getElementById('getPokemon');
const pokemonTeamContainer = document.getElementById('pokemonTeam');
const pokemonTeamatesContainer = document.getElementById('pokemonTeamates');
const pokemonTitleContainer = document.getElementById('pokemonTitle');

const getRandomPokemon = async () => {
    try {
    const randomPokemonId = Math.floor(Math.random() * 898) + 1;
    let response = await fetch(`https://pokeapi.co/api/v2/pokemon/${randomPokemonId}`);
    let data = await response.json()
    let spriteUrl = (data.sprites.front_default);
    const img = document.createElement('img');
    img.src = spriteUrl;
    pokemonTeamContainer.innerHTML = ''; // Clear previous content
    pokemonTeamContainer.appendChild(img);
    //get the type of pokemon
    let type = (data.types[0].type.name)
    const pokemonType = document.createElement('h6');
    pokemonTitleContainer.appendChild(pokemonType)
    pokemonType.innerText=`Pokemon Type: ${type}`
    //request all pokemons of that type
    let responseData = await fetch(`https://pokeapi.co/api/v2/type/${type}`);
    let typeData = await responseData.json()
    //get the list of pokemon of that type
    pokemonTeamatesContainer.innerHTML = ''    
    for (let i = 0; i < 5; i++) {
        let pokemon = typeData.pokemon[i].pokemon.name;
        await getPokemonSprite(pokemon);  

    }
}catch (err) {
        console.log(err.message)
    }
}
const getPokemonSprite = async (pokemon) => {
    try {
        let response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`);
        let data = await response.json();
        let spriteUrl = data.sprites.front_default;
        const img = document.createElement('img');
        img.src = spriteUrl;
       ; // Clear previous content
        pokemonTeamatesContainer.appendChild(img);
    } catch (err) {
        console.log(err.message);
    }
};

getButton.addEventListener('click', getRandomPokemon);