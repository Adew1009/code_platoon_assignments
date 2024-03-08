import { useEffect } from "react"; // Import useEffect
import { useOutletContext } from "react-router-dom";
import { Row, Col } from "react-bootstrap";
import FavoritesCard from "../components/favoritesCard";

const FavoritesPage = () => {
  // Remove favorites from the function parameters
  const { setFavorites, favorites } = useOutletContext();
  console.log(favorites);

  return (
    <>
      <h2 className="text-warning">Favorites</h2>
      <Row className="d-flex justify-content-center align-content-between flex-wrap">
        {/* Check if favorites is truthy before trying to render */}
        {favorites &&
          favorites.map((character) => (
            <Col key={character.id}>
              <FavoritesCard
                id={character.id}
                name={character.name}
                image={character.image}
                setFavorites={setFavorites}
                favorites={favorites}
                key={character.id}
              />
              <br />
            </Col>
          ))}
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
      </Row>
    </>
  );
};

export default FavoritesPage;
