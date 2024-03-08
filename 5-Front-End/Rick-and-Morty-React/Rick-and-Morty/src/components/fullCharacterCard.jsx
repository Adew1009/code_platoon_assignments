import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";

function FullCharacterCard(props) {
  return (
    <Card style={{ width: "40rem" }} data-bs-theme="dark">
      <Card.Body>
        <Card.Title className="text-info">{props.name}</Card.Title>
      </Card.Body>
      <Card.Img variant="top" src={props.image} />
      <ListGroup className="list-group-flush">
        <ListGroup.Item>Species: {props.species}</ListGroup.Item>
        <ListGroup.Item>Status: {props.status}</ListGroup.Item>
        <ListGroup.Item>Location: {props.location}</ListGroup.Item>
        <ListGroup.Item>Type: {props.type}</ListGroup.Item>
        <ListGroup.Item>Gender: {props.gender}</ListGroup.Item>
        <ListGroup.Item>Origin: {props.origin}</ListGroup.Item>
        <ListGroup.Item>Episodes: {props.episode}</ListGroup.Item>
      </ListGroup>
    </Card>
  );
}

export default FullCharacterCard;
