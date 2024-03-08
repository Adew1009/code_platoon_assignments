import { useEffect, useState } from "react";
import FullCharacterCard from "../components/fullCharacterCard";
import axios from "axios";
import { useParams, useOutletContext } from "react-router-dom";

const ACharacterPage = () => {
  const [aCharacter, setACharacter] = useState({});
  const { id } = useParams();
  // const { setFavorites, favorites } = useOutletContext();

  const getACharacter = async () => {
    try {
      let response = await axios.get(
        `https://rickandmortyapi.com/api/character/${id}`
      );
      setACharacter({
        name: response.data.name,
        image: response.data.image,
        species: response.data.species,
        status: response.data.status,
        location: response.data.location.name,
        type: response.data.type,
        gender: response.data.gender,
        origin: response.data.origin.name,
        episode: response.data.episode.map((episode) => episode),
      });

      console.log(response.data);
    } catch (error) {
      console.error("An error occurred:", error);
    }
  };

  useEffect(() => {
    getACharacter();
  }, []);

  return (
    <div className="d-flex justify-content-center m-9">
      <div>
        <FullCharacterCard
          image={aCharacter.image}
          name={aCharacter.name}
          species={aCharacter.species}
          status={aCharacter.status}
          location={aCharacter.location}
          type={aCharacter.type}
          gender={aCharacter.gender}
          origin={aCharacter.origin}
          episode={aCharacter.episode}
        />
      </div>
    </div>
  );
};

export default ACharacterPage;
