import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Products from "./pages/Products";
import Customers from "./pages/Customers";
import Orders from "./pages/Orders";
import Register from "./pages/Register";

import ProtectedRoute from "./components/ProtectedRoute";
import MainLayout from "./layouts/MainLayout";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/login"
          element={<Login />}
        />
        <Route
          path="/register"
          element={<Register />}
        />

        <Route
          path="/"
          element={
            <ProtectedRoute>
              <MainLayout />
            </ProtectedRoute>
          }
        >

          <Route
            index
            element={<Dashboard />}
          />

          <Route
            path="products"
            element={<Products />}
          />

          <Route
            path="customers"
            element={<Customers />}
          />

          <Route
            path="orders"
            element={<Orders />}
          />

        </Route>

        <Route
          path="*"
          element={
            <Navigate
              to="/"
              replace
            />
          }
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;