import { useEffect } from "react";
import { useState } from "react";

import ProductForm from "../components/ProductForm";
import ProductTable from "../components/ProductTable";

import {
  getProducts,
  createProduct,
  deleteProduct,
} from "../services/productService";

function Products() {

  const [products, setProducts] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts =
    async () => {

      try {

        setLoading(true);

        const data =
          await getProducts();

        setProducts(data);

      } catch {

        setError(
          "Failed to load products"
        );

      } finally {

        setLoading(false);
      }
    };

  const handleCreate =
    async (payload) => {

      try {

        await createProduct(
          payload
        );

        await loadProducts();

      } catch (error) {

        alert(
          error.response?.data?.detail ||
          "Failed to create product"
        );
      }
    };

  const handleDelete =
    async (id) => {

      const confirmed =
        window.confirm(
          "Delete this product?"
        );

      if (!confirmed) {
        return;
      }

      try {

        await deleteProduct(id);

        await loadProducts();

      } catch (error) {

        alert(
          error.response?.data?.detail ||
          "Failed to delete product"
        );
      }
    };

  if (loading) {

    return (
      <h2>
        Loading products...
      </h2>
    );
  }

  if (error) {

    return (
      <h2>
        {error}
      </h2>
    );
  }

  return (

    <div>

      <div
        style={{
          marginBottom: "24px",
        }}
      >
        <h1>
          Product Management
        </h1>

        <p
          style={{
            color: "#6b7280",
          }}
        >
          Manage inventory items,
          pricing, and stock levels.
        </p>
      </div>

      <ProductForm
        onCreate={
          handleCreate
        }
      />

      <div
        style={{
          marginBottom: "12px",
          fontWeight: "600",
        }}
      >
        Total Products:
        {" "}
        {products.length}
      </div>

      <ProductTable
        products={products}
        onDelete={
          handleDelete
        }
      />

    </div>
  );
}

export default Products;