import { Navigate } from "react-router-dom";

function ProtectedRoute(
  { children }
) {

  const token =
    localStorage.getItem(
      "access_token"
    );

  if (!token) {

    return (
      <Navigate
        to="/login"
        replace
      />
    );
  }

  try {

    const payload =
      JSON.parse(
        atob(
          token.split(".")[1]
        )
      );

    const now =
      Date.now() / 1000;

    if (
      payload.exp &&
      payload.exp < now
    ) {

      localStorage.removeItem(
        "access_token"
      );

      return (
        <Navigate
          to="/login"
          replace
        />
      );
    }

  } catch {

    localStorage.removeItem(
      "access_token"
    );

    return (
      <Navigate
        to="/login"
        replace
      />
    );
  }

  return children;
}

export default ProtectedRoute;