import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import RickPage from "./pages/rick";
import ErrorPage from "./pages/ErrorPage";
import CharactersPage from "./pages/CharactersPage";
import AboutPage from "./pages/AboutPage";

const router = createBrowserRouter ([
    {
        path: "/",
        element: <App/>,
        children: [
                {
                index: true,
                element: <HomePage/>
                },
                {
                    path: "about/",
                    element: < AboutPage/>
                },
                {
                    path: "characters-page/",
                    element: < CharactersPage/>
                },
                {
                    path: "rick/",
                    element: < RickPage/>
                }
        ],
        errorElement: <ErrorPage/>
    }
])
export default router;