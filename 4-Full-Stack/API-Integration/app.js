

const getPokemon = async(event) => {
    try{
        event.preventDefault()
        let form = new FormData(event.target)
        let formData = Object.fromEntries(form)
        console.log(typeof(formData), console.log(formData))
        let response = await fetch(`https://pokeapi.co/api/v2/pokemon/${formData.pokemon}`)
        let responseData = await response.json()
        console.log(responseData.sprites)
        let img = document.getElementById("pokemonImg")
        let img2 = document.getElementById("pokemonImg2")
        let name = document.getElementById("pokemonName")
        name.innerText = responseData.name.toUpperCase()
        img.src = responseData.sprites.front_default
        img.style.border = "5px yellow solid"
        img.style.borderRadius = "20px"
        img.style.height = "325px"
        img.style.backgroundColor = "white"
        img2.src = responseData.sprites.front_shiny
        img2.style.border = "5px gold solid"
        img2.style.borderRadius = "20px"
        img2.style.height = "325px"
        img2.style.backgroundColor = "white"
    } 
    catch(err){
        console.log(err.message)
    }
}