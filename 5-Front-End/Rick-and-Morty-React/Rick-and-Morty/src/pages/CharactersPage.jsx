import { useEffect, useState } from "react";
import CharacterCard from "../components/charactercard";
import axios from "axios";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const CharactersPage = () => {
  const [allCharacters, setAllCharacters] = useState([]);

  const getAllCharacters = async () => {
    let num = 1;
    let tempData = [];
    while (num < 43) {
      try {
        let response = await axios.get(
          "https://rickandmortyapi.com/api/character/"
        );
        let results = response.data.results;
        tempData = [...tempData, ...results];
        //TODO     why do they both need the spread?
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
      <row className="d-flex justify-content-center align-content-betwe flex-wrap">
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
              species={characterObject.species}
              status={characterObject.status}
              location={characterObject.location.name}
              key={index}
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
