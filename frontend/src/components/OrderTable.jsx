import { useState } from "react";

function OrderTable({
  orders,
  onDelete,
}) {

  const role =
    localStorage.getItem(
      "role"
    );

  const [search,
    setSearch] =
    useState("");

  const filteredOrders =
    orders.filter(
      (order) =>
        String(
          order.id
        ).includes(
          search
        ) ||
        String(
          order.customer_id
        ).includes(
          search
        )
    );

  if (
    orders.length === 0
  ) {
    return (
      <div
        style={{
          background:
            "#fff",
          padding: "40px",
          borderRadius:
            "12px",
          textAlign:
            "center",
        }}
      >
        No orders found.
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
          placeholder="Search Order..."
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
          Total Orders:
          {" "}
          {orders.length}
        </strong>

      </div>

      <div
        style={{
          overflowX:
            "auto",
          backgroundColor:
            "#ffffff",
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
                backgroundColor:
                  "#f9fafb",
              }}
            >
              <th style={thStyle}>
                ID
              </th>

              <th style={thStyle}>
                Customer
              </th>

              <th style={thStyle}>
                Amount
              </th>

              <th style={thStyle}>
                Status
              </th>

              <th style={thStyle}>
                Action
              </th>
            </tr>
          </thead>

          <tbody>

            {filteredOrders.map(
              (order) => (

                <tr
                  key={
                    order.id
                  }
                  style={{
                    borderBottom:
                      "1px solid #e5e7eb",
                  }}
                >

                  <td style={tdStyle}>
                    {order.id}
                  </td>

                  <td style={tdStyle}>
                    {
                      order.customer_id
                    }
                  </td>

                  <td style={tdStyle}>
                    ₹
                    {
                      order.total_amount
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
                          order.status ===
                          "COMPLETED"
                            ? "#dcfce7"
                            : "#fef3c7",
                        color:
                          order.status ===
                          "COMPLETED"
                            ? "#15803d"
                            : "#d97706",
                        fontWeight:
                          "600",
                      }}
                    >
                      {
                        order.status
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
                                "Delete this order?"
                              );

                            if (
                              confirmed
                            ) {

                              onDelete(
                                order.id
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

export default OrderTable;