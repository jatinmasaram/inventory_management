import { useEffect } from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {Link} from "react-router-dom";

import { login } from "../services/authService";

function Login() {

  const navigate =
    useNavigate();

  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const [error, setError] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  useEffect(() => {

    const token =
      localStorage.getItem(
        "access_token"
      );

    if (token) {
      navigate("/");
    }

  }, [navigate]);

  const handleSubmit =
    async (e) => {

      e.preventDefault();

      setError("");
      setLoading(true);

      try {

        const result =
          await login(
            email,
            password
          );

        localStorage.setItem(
          "access_token",
          result.access_token
        );

        localStorage.setItem(
          "role",
          result.user.role
        );

        navigate("/");

      } catch (error) {

        setError(
          error.response?.data?.detail ||
          "Invalid credentials"
        );

      } finally {

        setLoading(false);
      }
    };

  return (

    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor:
          "#f3f4f6",
      }}
    >

      <div
        style={{
          width: "420px",
          backgroundColor:
            "#ffffff",
          padding: "32px",
          borderRadius: "16px",
          boxShadow:
            "0 10px 25px rgba(0,0,0,0.08)",
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
          Secure Login
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
            style={inputStyle}
            required
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) =>
              setPassword(
                e.target.value
              )
            }
            style={inputStyle}
            required
          />

          <button
            type="submit"
            disabled={loading}
            style={buttonStyle}
          >

            {
              loading
                ? "Signing In..."
                : "Login"
            }
          </button>

          {
            error && (
              <p
                style={{
                  color:
                    "#dc2626",
                }}
              >
                {error}
              </p>
            )
          }

        </form>

        <br />

        <Link to="/register">
          Don't have an account? Register
        </Link>

      </div>

    </div>
  );
}

const inputStyle = {
  width: "100%",
  padding: "12px",
  marginBottom: "16px",
  borderRadius: "8px",
  border: "1px solid #d1d5db",
  boxSizing: "border-box",
};

const buttonStyle = {
  width: "100%",
  padding: "12px",
  backgroundColor: "#2563eb",
  color: "#ffffff",
  border: "none",
  borderRadius: "8px",
  cursor: "pointer",
  fontWeight: "600",
};

export default Login;