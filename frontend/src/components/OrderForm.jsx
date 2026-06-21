import { useState } from "react";

function OrderForm({
  onCreate,
}) {

  const role =
    localStorage.getItem(
      "role"
    );

  const [
    customerId,
    setCustomerId,
  ] = useState("");

  const [
    productId,
    setProductId,
  ] = useState("");

  const [
    quantity,
    setQuantity,
  ] = useState("");

  const [
    submitting,
    setSubmitting,
  ] = useState(false);


  const handleSubmit =
    async (e) => {

      e.preventDefault();

      if (
        Number(quantity) <= 0
      ) {
        alert(
          "Quantity must be greater than zero"
        );
        return;
      }

      try {

        setSubmitting(
          true
        );

        await onCreate({
          customer_id:
            Number(
              customerId
            ),
          items: [
            {
              product_id:
                Number(
                  productId
                ),
              quantity:
                Number(
                  quantity
                ),
            },
          ],
        });

        setCustomerId("");
        setProductId("");
        setQuantity("");

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
        Create Order
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
          type="number"
          placeholder="Customer ID"
          value={customerId}
          onChange={(e)=>
            setCustomerId(
              e.target.value
            )
          }
          style={inputStyle}
          required
        />

        <input
          type="number"
          placeholder="Product ID"
          value={productId}
          onChange={(e)=>
            setProductId(
              e.target.value
            )
          }
          style={inputStyle}
          required
        />

        <input
          type="number"
          min="1"
          placeholder="Quantity"
          value={quantity}
          onChange={(e)=>
            setQuantity(
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
              : "Create Order"
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
  color: "#ffffff",
  border: "none",
  borderRadius: "8px",
  padding: "12px",
  cursor: "pointer",
  fontWeight: "600",
};

export default OrderForm;