import { Link } from "react-router-dom";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";

const PageNavbar = () => {
  return (
    <>
      <Navbar className="sticky-top" bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand className="text-info" href="/">
            RICK & MORTY
          </Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link className="text-info" as={Link} to="/">
              Home
            </Nav.Link>
            <Nav.Link className="text-info" as={Link} to="/characters-page">
              Characters
            </Nav.Link>
            <Nav.Link className="text-info" as={Link} to="/about">
              About
            </Nav.Link>
            <Nav.Link className="text-info" as={Link} to="/favorites">
              Favorites
            </Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    </>
  );
  className = "text-info";
};

export default PageNavbar;

// <span>
//   <Link to="/">Home</Link>
// </span>
