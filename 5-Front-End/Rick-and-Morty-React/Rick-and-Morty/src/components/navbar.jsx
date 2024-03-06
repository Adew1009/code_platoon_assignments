import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <span>
        <div>
      <Link to="/">Home</Link>
      </div>
      <Link to="rick/">Rick</Link>
    </span>
  );
};

export default Navbar;
