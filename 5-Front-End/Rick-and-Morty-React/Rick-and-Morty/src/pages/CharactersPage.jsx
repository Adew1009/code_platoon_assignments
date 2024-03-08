import { useEffect, useState } from "react";
import CharacterCard from "../components/charactercard";
import axios from "axios";
import { useOutletContext } from "react-router-dom";

const CharactersPage = () => {
  const [allCharacters, setAllCharacters] = useState([]);
  const { favorites, setFavorites, addToFavorites, removeFromFavorites } =
    useOutletContext();

  const getAllCharacters = async () => {
    let num = 1;
    let tempData = [];
    while (num < 43) {
      try {
        let response = await axios.get(
          `https://rickandmortyapi.com/api/character/?page=${num}`
        );
        let results = response.data.results;
        tempData = [...tempData, ...results];
        num++;
      } catch (error) {
        console.error("An error occurred:", error);
      }
    }
    setAllCharacters(tempData);
  };
  useEffect(() => {
    getAllCharacters();
  }, []);

  return (
    <>
      <div>
        <h1 className="text-info" id="characters">
          {" "}
          Characters of Rick and Morty
        </h1>
      </div>
      <row className="d-flex justify-content-center align-content-betweeen flex-wrap">
        {allCharacters.map((characterObject, index) => (
          <div
            className="d-flex justify-content-top flex-wrap m-4 "
            id={index}
            key={index}
          >
            <br />
            <CharacterCard
              image={characterObject.image}
              name={characterObject.name}
              key={index}
              id={characterObject.id}
              setFavorites={setFavorites}
              favorites={favorites}
            />
            <br />
            <br />
            <br />
          </div>
        ))}
      </row>
    </>
  );
};
export default CharactersPage;
