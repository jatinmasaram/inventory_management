import { useState } from "react";

function CustomerTable({
  customers,
  onDelete,
}) {

  const role =
    localStorage.getItem(
      "role"
    );

  const [search,
    setSearch] =
    useState("");

  const filteredCustomers =
    customers.filter(
      (customer) =>
        customer.full_name
          .toLowerCase()
          .includes(
            search.toLowerCase()
          ) ||
        customer.email
          .toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  if (
    customers.length === 0
  ) {
    return (
      <div
        style={{
          background:
            "#fff",
          padding: "40px",
          textAlign:
            "center",
          borderRadius:
            "12px",
        }}
      >
        No customers found.
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
          placeholder="Search Customer..."
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
          Total Customers:
          {" "}
          {customers.length}
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
                Name
              </th>

              <th style={thStyle}>
                Email
              </th>

              <th style={thStyle}>
                Phone
              </th>

              <th style={thStyle}>
                Action
              </th>
            </tr>
          </thead>

          <tbody>

            {filteredCustomers.map(
              (
                customer
              ) => (
                <tr
                  key={
                    customer.id
                  }
                  style={{
                    borderBottom:
                      "1px solid #e5e7eb",
                  }}
                >
                  <td style={tdStyle}>
                    {
                      customer.id
                    }
                  </td>

                  <td style={tdStyle}>
                    {
                      customer.full_name
                    }
                  </td>

                  <td style={tdStyle}>
                    {
                      customer.email
                    }
                  </td>

                  <td style={tdStyle}>
                    {
                      customer.phone
                    }
                  </td>

                  <td style={tdStyle}>

                    {
                      role ===
                      "ADMIN" && (
                        <button
                          onClick={() => {

                            const confirmed =
                              window.confirm(
                                "Delete this customer?"
                              );

                            if (
                              confirmed
                            ) {
                              onDelete(
                                customer.id
                              );
                            }
                          }}
                          style={{
                            backgroundColor:
                              "#ef4444",
                            color:
                              "#ffffff",
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

export default CustomerTable;