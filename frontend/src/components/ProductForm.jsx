import { useState } from "react";

function ProductForm({
  onCreate,
}) {

  const [name, setName] =
    useState("");

  const [sku, setSku] =
    useState("");

  const [price, setPrice] =
    useState("");

  const [
    stockQuantity,
    setStockQuantity,
  ] = useState("");

  const [submitting,
    setSubmitting] =
    useState(false);

  const role =
    localStorage.getItem(
      "role"
    );



  const handleSubmit =
    async (e) => {

      e.preventDefault();

      try {

        setSubmitting(true);

        await onCreate({
          name,
          sku,
          price:
            Number(price),
          stock_quantity:
            Number(
              stockQuantity
            ),
        });

        setName("");
        setSku("");
        setPrice("");
        setStockQuantity("");

      } finally {

        setSubmitting(
          false
        );
      }
    };

  return (
    <div
      style={{
        backgroundColor:
          "#ffffff",
        padding: "24px",
        borderRadius:
          "12px",
        boxShadow:
          "0 2px 8px rgba(0,0,0,0.08)",
        marginBottom:
          "24px",
      }}
    >
      <h3>
        Add Product
      </h3>

      <form
        onSubmit={
          handleSubmit
        }
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fit,minmax(220px,1fr))",
          gap: "16px",
        }}
      >

        <input
          placeholder="Product Name"
          value={name}
          onChange={(e)=>
            setName(
              e.target.value
            )
          }
          style={inputStyle}
          required
        />

        <input
          placeholder="SKU"
          value={sku}
          onChange={(e)=>
            setSku(
              e.target.value
            )
          }
          style={inputStyle}
          required
        />

        <input
          type="number"
          placeholder="Price"
          value={price}
          onChange={(e)=>
            setPrice(
              e.target.value
            )
          }
          style={inputStyle}
          required
        />

        <input
          type="number"
          placeholder="Stock Quantity"
          value={
            stockQuantity
          }
          onChange={(e)=>
            setStockQuantity(
              e.target.value
            )
          }
          style={inputStyle}
          required
        />

        <button
          type="submit"
          disabled={
            submitting
          }
          style={{
            ...buttonStyle,
            opacity:
              submitting
                ? 0.7
                : 1,
          }}
        >
          {
            submitting
              ? "Creating..."
              : "Create Product"
          }
        </button>

      </form>
    </div>
  );
}

const inputStyle = {
  padding: "12px",
  border:
    "1px solid #d1d5db",
  borderRadius: "8px",
};

const buttonStyle = {
  backgroundColor:
    "#2563eb",
  color: "#fff",
  border: "none",
  borderRadius: "8px",
  padding: "12px",
  cursor: "pointer",
  fontWeight: "600",
};

export default ProductForm;