import { useState } from "react";
import {
  useNavigate,
  Link,
} from "react-router-dom";

import {
  register,
} from "../services/authService";

function Register() {

  const navigate =
    useNavigate();

  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const [error, setError] =
    useState("");

  const handleSubmit =
    async (e) => {

      e.preventDefault();

      try {

        const result =
          await register(
            email,
            password
          );

        localStorage.setItem(
          "access_token",
          result.access_token
        );

        navigate("/");

      } catch {

        setError(
          "Registration failed"
        );
      }
    };

  return (
    <div
      style={{
        maxWidth: "400px",
        margin: "50px auto",
      }}
    >
      <h1>
        InventoryMS
      </h1>

      <p
        style={{
          color: "#6b7280",
        }}
      >
        Create Account
      </p>

      <form
        onSubmit={
          handleSubmit
        }
      >

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(
              e.target.value
            )
          }
          required
          style={inputStyle}
        />

        <br />
        <br />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(
              e.target.value
            )
          }
          required
          style={inputStyle}
        />

        <br />
        <br />

        <button
          type="submit"
          style={buttonStyle}
        >
          Register
        </button>

        {error && (
          <p
            style={{
              color: "red",
            }}
          >
            {error}
          </p>
        )}

      </form>

      <br />

      <Link to="/login">
        Already have an account? Login
      </Link>

    </div>
  );
}

const inputStyle = {
  width: "100%",
  padding: "14px",
  border: "1px solid #d1d5db",
  borderRadius: "8px",
  fontSize: "16px",
  boxSizing: "border-box",
};

const buttonStyle = {
  width: "100%",
  backgroundColor: "#2563eb",
  color: "#ffffff",
  border: "none",
  padding: "14px",
  borderRadius: "8px",
  cursor: "pointer",
  fontWeight: "600",
  fontSize: "16px",
};

export default Register;