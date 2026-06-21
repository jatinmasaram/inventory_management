import { useState } from "react";

function CustomerForm({
  onCreate,
}) {

  const [
    fullName,
    setFullName,
  ] = useState("");

  const [email,
    setEmail] =
    useState("");

  const [phone,
    setPhone] =
    useState("");

  const [
    submitting,
    setSubmitting,
  ] = useState(false);

  const role =
    localStorage.getItem(
      "role"
    );



  const handleSubmit =
    async (e) => {

      e.preventDefault();

      try {

        setSubmitting(
          true
        );

        await onCreate({
          full_name:
            fullName,
          email,
          phone,
        });

        setFullName("");
        setEmail("");
        setPhone("");

      } finally {

        setSubmitting(
          false
        );
      }
    };

  return (
    <div
      style={{
        backgroundColor: "#ffffff",
        padding: "24px",
        borderRadius: "12px",
        boxShadow:
          "0 2px 8px rgba(0,0,0,0.08)",
        marginBottom: "24px",
        width: "100%",
        boxSizing: "border-box",
      }}
    >
      <h3>
        Add Customer
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
          placeholder="Full Name"
          value={fullName}
          onChange={(e)=>
            setFullName(
              e.target.value
            )
          }
          style={inputStyle}
          required
        />

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e)=>
            setEmail(
              e.target.value
            )
          }
          style={inputStyle}
          required
        />

        <input
          placeholder="Phone Number"
          value={phone}
          onChange={(e)=>
            setPhone(
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
              : "Create Customer"
          }
        </button>

      </form>
    </div>
  );
}

const inputStyle = {
  width: "100%",
  padding: "12px",
  border: "1px solid #d1d5db",
  borderRadius: "8px",
  boxSizing: "border-box",
};

const buttonStyle = {
  width: "100%",
  backgroundColor: "#2563eb",
  color: "#fff",
  border: "none",
  borderRadius: "8px",
  padding: "12px",
  cursor: "pointer",
  fontWeight: "600",
};

export default CustomerForm;