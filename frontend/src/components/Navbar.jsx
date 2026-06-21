import {
  Link,
  useNavigate,
  useLocation,
} from "react-router-dom";

function Navbar() {

  const navigate =
    useNavigate();

  const location =
    useLocation();

  const role =
    localStorage.getItem(
      "role"
    );

  const logout = () => {

    localStorage.removeItem(
      "access_token"
    );

    localStorage.removeItem(
      "role"
    );

    navigate(
      "/login"
    );
  };

  const navStyle = (
    path
  ) => ({

    textDecoration:
      "none",

    color:
      location.pathname === path
        ? "#2563eb"
        : "#374151",

    backgroundColor:
      location.pathname === path
        ? "#eff6ff"
        : "transparent",

    fontWeight:
      location.pathname === path
        ? "600"
        : "500",

    padding:
      "10px 14px",

    borderRadius:
      "8px",

    transition:
      "all 0.2s ease",
  });

  return (

    <nav
      style={{
        position:
          "sticky",

        top: 0,

        zIndex: 1000,

        backgroundColor:
          "#ffffff",

        borderBottom:
          "1px solid #e5e7eb",

        padding:
          "16px 32px",

        display: "flex",
        alignItems: "center",
        gap: "20px",
        flexWrap: "wrap",

        boxShadow:
          "0 2px 8px rgba(0,0,0,0.05)",
      }}
    >

      <h2
        style={{
          margin: 0,
          color:
            "#111827",
        }}
      >
        InventoryMS
      </h2>

      <Link
        to="/"
        style={navStyle("/")}
      >
        Dashboard
      </Link>

      <Link
        to="/products"
        style={navStyle("/products")}
      >
        Products
      </Link>

      <Link
        to="/customers"
        style={navStyle("/customers")}
      >
        Customers
      </Link>

      <Link
        to="/orders"
        style={navStyle("/orders")}
      >
        Orders
      </Link>

      <div
        style={{
          marginLeft:
            "auto",

          display:
            "flex",

          alignItems:
            "center",

          gap:
            "12px",
        }}
      >

        <span
          style={{
            backgroundColor:
              role === "ADMIN"
                ? "#dcfce7"
                : "#dbeafe",

            color:
              role === "ADMIN"
                ? "#166534"
                : "#1d4ed8",

            padding:
              "8px 14px",

            borderRadius:
              "999px",

            fontWeight:
              "600",

            fontSize:
              "14px",
          }}
        >
          {role}
        </span>

        <button
          onClick={
            logout
          }
          style={{
            backgroundColor:
              "#ef4444",

            color:
              "white",

            border:
              "none",

            padding:
              "10px 16px",

            borderRadius:
              "8px",

            cursor:
              "pointer",

            fontWeight:
              "600",
          }}
        >
          Logout
        </button>

      </div>

    </nav>
  );
}

export default Navbar;