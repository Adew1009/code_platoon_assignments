import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import ErrorPage from "./pages/ErrorPage";
import CharactersPage from "./pages/CharactersPage";
import ACharacterPage from "./pages/ACharacter";
import AboutPage from "./pages/AboutPage";
import { useParams } from "react-router-dom";
import FavoritesPage from "./pages/FavoritesPage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: <HomePage />,
      },
      {
        path: "about/",
        element: <AboutPage />,
      },
      {
        path: "characters-page/",
        element: <CharactersPage />,
      },
      {
        path: "character/:id",
        element: <ACharacterPage />,
      },
      {
        path: "favorites/",
        element: <FavoritesPage />,
      },
    ],
    errorElement: <ErrorPage />,
  },
]);
export default router;
