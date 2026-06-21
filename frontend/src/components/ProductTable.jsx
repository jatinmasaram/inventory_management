import { useState } from "react";

function ProductTable({
  products,
  onDelete,
}) {

  const role =
    localStorage.getItem(
      "role"
    );

  const [search,
    setSearch] =
    useState("");

  const filteredProducts =
    products.filter(
      (product) =>
        product.name
          .toLowerCase()
          .includes(
            search.toLowerCase()
          ) ||
        product.sku
          .toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  if (
    products.length === 0
  ) {

    return (
      <div
        style={{
          padding: "40px",
          textAlign:
            "center",
          background:
            "#fff",
          borderRadius:
            "12px",
        }}
      >
        No products found.
      </div>
    );
  }

  return (
    <div>

      <div
        style={{
          display: "flex",
          justifyContent:
            "space-between",
          marginBottom:
            "12px",
        }}
      >
        <input
          placeholder="Search Product..."
          value={search}
          onChange={(e)=>
            setSearch(
              e.target.value
            )
          }
          style={{
            padding:
              "10px",
            width:
              "300px",
            border:
              "1px solid #ddd",
            borderRadius:
              "8px",
          }}
        />

        <strong>
          Total Products:
          {" "}
          {products.length}
        </strong>

      </div>

      <div
        style={{
          overflowX:
            "auto",
          background:
            "#fff",
          borderRadius:
            "12px",
          boxShadow:
            "0 2px 8px rgba(0,0,0,0.08)",
        }}
      >

        <table
          style={{
            width: "100%",
            borderCollapse:
              "collapse",
          }}
        >

          <thead>
            <tr
              style={{
                background:
                  "#f9fafb",
              }}
            >
              <th style={thStyle}>ID</th>
              <th style={thStyle}>Name</th>
              <th style={thStyle}>SKU</th>
              <th style={thStyle}>Price</th>
              <th style={thStyle}>Stock</th>
              <th style={thStyle}>Action</th>
            </tr>
          </thead>

          <tbody>

            {filteredProducts.map(
              (
                product
              ) => (

                <tr
                  key={
                    product.id
                  }
                  style={{
                    borderBottom:
                      "1px solid #e5e7eb",
                    backgroundColor:
                      product.stock_quantity <= 10
                        ? "#fff7ed"
                        : "white",
                  }}
                >

                  <td style={tdStyle}>
                    {
                      product.id
                    }
                  </td>

                  <td style={tdStyle}>
                    {
                      product.name
                    }
                  </td>

                  <td style={tdStyle}>
                    {
                      product.sku
                    }
                  </td>

                  <td style={tdStyle}>
                    ₹
                    {
                      product.price
                    }
                  </td>

                  <td style={tdStyle}>
                    <span
                      style={{
                        padding:
                          "4px 10px",
                        borderRadius:
                          "20px",
                        backgroundColor:
                          product.stock_quantity <= 10
                            ? "#fee2e2"
                            : "#dcfce7",
                        color:
                          product.stock_quantity <= 10
                            ? "#dc2626"
                            : "#16a34a",
                        fontWeight:
                          "600",
                      }}
                    >
                      {
                        product.stock_quantity
                      }
                    </span>
                  </td>

                  <td style={tdStyle}>

                    {
                      true && (

                        <button
                          onClick={() => {

                            const confirmed =
                              window.confirm(
                                "Delete this product?"
                              );

                            if (
                              confirmed
                            ) {

                              onDelete(
                                product.id
                              );
                            }
                          }}
                          style={{
                            backgroundColor:
                              "#ef4444",
                            color:
                              "#fff",
                            border:
                              "none",
                            padding:
                              "8px 12px",
                            borderRadius:
                              "6px",
                            cursor:
                              "pointer",
                          }}
                        >
                          Delete
                        </button>
                      )
                    }

                  </td>

                </tr>
              )
            )}

          </tbody>

        </table>

      </div>

    </div>
  );
}

const thStyle = {
  textAlign: "left",
  padding: "14px",
  color: "#374151",
  fontWeight: "600",
};

const tdStyle = {
  padding: "14px",
  color: "#111827",
};

export default ProductTable;