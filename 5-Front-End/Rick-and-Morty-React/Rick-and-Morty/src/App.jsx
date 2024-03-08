import { useState } from "react";
import "./App.css";
import PageNavbar from "./components/navbar";
import { Outlet } from "react-router-dom";
import { useOutletContext } from "react-router-dom";
import FavoritesCard from "./components/favoritesCard";
import { Alert } from "react-bootstrap";
import WarningBox from "./components/warningBox";

function App() {
  const [favorites, setFavorites] = useState([]);
  const [showAlert, setShowAlert] = useState(false); // State to control the visibility of the alert

  const addToFavorites = (character) => {
    // Check if the character is already in favorites
    const isCharacterInFavorites = favorites.some((c) => c.id === character.id);

    // If there are already 4 favorites, display a warning message
    if (favorites.length >= 4) {
      setShowAlert(true); // Show the alert
    } else {
      // If the character is not already in favorites, add it
      if (!isCharacterInFavorites) {
        const updatedFavorites = [
          ...favorites,
          { id: character.id, name: character.name, image: character.image },
        ];
        setFavorites(updatedFavorites); // Update favorites state
      }
    }
  };

  const removeFromFavorites = (characterID) => {
    const updatedFavorites = favorites.filter((c) => c.id !== characterID);
    setFavorites(updatedFavorites);
  };

  const determineFavorite = (characterID) => {
    return favorites.some((c) => c.id === characterID);
  };

  return (
    <main>
      <Alert
        className="fixed-top"
        show={showAlert}
        variant="danger"
        onClose={() => setShowAlert(false)}
        dismissible
      >
        <Alert.Heading>
          Oh Jeez! You did it now! You got an error!
        </Alert.Heading>
        <p>
          You can only have 4 four favorites! You will need to send some back to
          another dimension to pick this one.{" "}
        </p>
      </Alert>
      <div id="App">
        <PageNavbar />
        <div>
          <Outlet
            context={{
              favorites,
              setFavorites,
              addToFavorites,
              removeFromFavorites,
              determineFavorite,
            }}
          />
        </div>
      </div>
    </main>
  );
}
export default App;
