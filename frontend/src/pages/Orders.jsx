import { useEffect } from "react";
import { useState } from "react";

import OrderForm from "../components/OrderForm";
import OrderTable from "../components/OrderTable";

import {
  getOrders,
  createOrder,
  deleteOrder,
} from "../services/orderService";

function Orders() {

  const [orders, setOrders] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  useEffect(() => {
    loadOrders();
  }, []);

  const loadOrders =
    async () => {

      try {

        setLoading(true);

        const data =
          await getOrders();

        setOrders(data);

      } catch {

        setError(
          "Failed to load orders"
        );

      } finally {

        setLoading(false);
      }
    };

  const handleCreate =
    async (payload) => {

      try {

        await createOrder(
          payload
        );

        await loadOrders();

      } catch (error) {

        alert(
          error.response?.data?.detail ||
          "Failed to create order"
        );
      }
    };

  const handleDelete =
    async (id) => {

      const confirmed =
        window.confirm(
          "Delete this order?"
        );

      if (!confirmed) {
        return;
      }

      try {

        await deleteOrder(id);

        await loadOrders();

      } catch (error) {

        alert(
          error.response?.data?.detail ||
          "Failed to delete order"
        );
      }
    };

  if (loading) {

    return (
      <h2>
        Loading orders...
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
          Order Management
        </h1>

        <p
          style={{
            color: "#6b7280",
          }}
        >
          Create and monitor
          customer orders.
        </p>
      </div>

      <OrderForm
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
        Total Orders:
        {" "}
        {orders.length}
      </div>

      <OrderTable
        orders={orders}
        onDelete={
          handleDelete
        }
      />

    </div>
  );
}

export default Orders;