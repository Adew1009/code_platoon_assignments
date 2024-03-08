import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import { useOutletContext } from "react-router-dom";

function FavoritesCard(props) {
  const {
    setFavorites,
    favorites,
    addToFavorites,
    removeFromFavorites,
    determineFavorite,
  } = useOutletContext();

  return (
    <Card border="primary" style={{ width: "30rem" }} data-bs-theme="dark">
      <Card.Body>
        <Card.Title className="text-info">
          Your Favorite: {props.name}
        </Card.Title>
      </Card.Body>
      <Card.Img variant="top" src={props.image} />
      <ListGroup className="list-group-flush"></ListGroup>
      <Card.Title as={Link} to={`/character/${props.id}`} className="text-info">
        More Details
      </Card.Title>
      <Button
        variant="info"
        onClick={() => {
          removeFromFavorites(props.id);
        }}
      >
        Remove From Favorites
      </Button>
    </Card>
  );
}

export default FavoritesCard;
