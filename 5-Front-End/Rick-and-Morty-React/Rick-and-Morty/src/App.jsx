import { useState } from "react";
import "./App.css";
import PageNavbar from "./components/navbar";
import { Outlet } from "react-router-dom";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div id="App">
      <PageNavbar />

      <div>
        <Outlet />
      </div>
    </div>
  );
}

export default App;
