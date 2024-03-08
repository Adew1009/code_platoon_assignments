import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import { useOutletContext } from "react-router-dom";

function CharacterCard(props) {
  const {
    setFavorites,
    favorites,
    addToFavorites,
    removeFromFavorites,
    determineFavorite,
  } = useOutletContext();

  const isCharacterInFavorites = favorites.some((c) => c.id === props.id);

  return (
    <Card
      style={{ width: "15rem" }}
      className={
        isCharacterInFavorites
          ? "bg-info bg-opacity-75"
          : "bg-warning bg-opacity-75"
      }
    >
      <Card.Body>
        <Card.Title className="text-dark bg-image hover-zoom">
          {props.name}
        </Card.Title>
      </Card.Body>
      <Card.Img variant="top" src={props.image} />
      <ListGroup className="list-group-flush"></ListGroup>
      <Card.Title
        as={Link}
        to={`/character/${props.id}`}
        className="text-primary"
      >
        More Details
      </Card.Title>
      {/* Use ternary operator for conditional rendering */}
      {isCharacterInFavorites ? (
        <Button
          variant="danger"
          onClick={() => {
            removeFromFavorites(props.id);
          }}
        >
          Remove From Favorites
        </Button>
      ) : (
        <Button
          variant="primary"
          onClick={() => {
            addToFavorites(props);
          }}
        >
          Add To Favorites
        </Button>
      )}
    </Card>
  );
}

export default CharacterCard;
