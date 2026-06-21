import { Outlet }
from "react-router-dom";

import Navbar
from "../components/Navbar";

function MainLayout() {

  return (

    <div
      style={{
        minHeight:
          "100vh",

        backgroundColor:
          "#f3f4f6",
      }}
    >

      <Navbar />

      <main
        style={{
          padding: "2rem",
          width: "100%",
          maxWidth: "1400px",
          margin: "0 auto",
          boxSizing: "border-box",
        }}
      >

        <Outlet />

      </main>

    </div>
  );
}

export default MainLayout;