import { Link } from "react-router-dom";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";


const PageNavbar = () => {
  return (
    <>
      <Navbar className="sticky-top" bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand href="/">RICK & MORTY</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/characters-page">Characters</Nav.Link>
            <Nav.Link href="/about">About</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    </>
  );
};

export default PageNavbar;


    // <span>
    //   <Link to="/">Home</Link>
    // </span>
    