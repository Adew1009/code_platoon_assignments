import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";

function CharacterCard(props) {
  return (
    <Card style={{ width: "15rem" }} data-bs-theme="dark">
      <Card.Body>
        <Card.Title>{props.name}</Card.Title>
      </Card.Body>
      <Card.Img variant="top" src={props.image} />
      <ListGroup className="list-group-flush">
        <ListGroup.Item>Species: {props.species}</ListGroup.Item>
        <ListGroup.Item>Status: {props.status}</ListGroup.Item>
        <ListGroup.Item>Location: {props.location}</ListGroup.Item>
      </ListGroup>
    </Card>
  );
}

export default CharacterCard;
