import { useEffect, useState } from "react";

import CustomerForm from "../components/CustomerForm";
import CustomerTable from "../components/CustomerTable";

import {
  getCustomers,
  createCustomer,
  deleteCustomer,
} from "../services/customerService";

function Customers() {

  const [customers, setCustomers] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  useEffect(() => {
    loadCustomers();
  }, []);

  const loadCustomers =
    async () => {

      try {

        setLoading(true);

        const data =
          await getCustomers();

        setCustomers(data);

      } catch {

        setError(
          "Failed to load customers"
        );

      } finally {

        setLoading(false);
      }
    };

  const handleCreate =
    async (payload) => {

      try {

        await createCustomer(
          payload
        );

        await loadCustomers();

      } catch (error) {

        alert(
          error.response?.data?.detail ||
          "Failed to create customer"
        );
      }
    };

  const handleDelete =
    async (id) => {

      const confirmed =
        window.confirm(
          "Delete this customer?"
        );

      if (!confirmed) return;

      try {

        await deleteCustomer(id);

        await loadCustomers();

      } catch (error) {

        alert(
          error.response?.data?.detail ||
          "Failed to delete customer"
        );
      }
    };

  if (loading) {

    return (
      <h2>
        Loading customers...
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
          Customer Management
        </h1>

        <p
          style={{
            color: "#6b7280",
          }}
        >
          Manage customer records and relationships.
        </p>
      </div>

      <CustomerForm
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
        Total Customers:
        {" "}
        {customers.length}
      </div>

      <CustomerTable
        customers={customers}
        onDelete={
          handleDelete
        }
      />

    </div>
  );
}

export default Customers;