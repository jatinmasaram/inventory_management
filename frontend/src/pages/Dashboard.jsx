import { useEffect, useState } from "react";

import StatsCard from "../components/StatsCard";

import {
  getDashboardSummary,
} from "../services/dashboardService";

function Dashboard() {

  const [summary, setSummary] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard =
    async () => {

      try {

        const data =
          await getDashboardSummary();

        setSummary(data);

      } catch {

        setError(
          "Failed to load dashboard"
        );

      } finally {

        setLoading(false);
      }
    };

  if (loading) {

    return (
      <h2>
        Loading dashboard...
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
          marginBottom: "30px",
        }}
      >
        <h1>
          Inventory Dashboard
        </h1>

        <p
          style={{
            color: "#6b7280",
          }}
        >
          Monitor inventory,
          customers,
          orders,
          and stock health.
        </p>
      </div>

      <div
        style={{
          display: "flex",
          gap: "20px",
          flexWrap: "wrap",
        }}
      >

        <StatsCard
          title="Products"
          value={
            summary.total_products
          }
        />

        <StatsCard
          title="Customers"
          value={
            summary.total_customers
          }
        />

        <StatsCard
          title="Orders"
          value={
            summary.total_orders
          }
        />

        <StatsCard
          title="Low Stock"
          value={
            summary.low_stock_products
          }
        />

      </div>

      <div
        style={{
          marginTop: "40px",
          backgroundColor:
            "#ffffff",
          padding: "24px",
          borderRadius: "16px",
          boxShadow:
            "0 2px 8px rgba(0,0,0,0.08)",
        }}
      >

        <h3>
          Inventory Insights
        </h3>

        <ul
          style={{
            color: "#4b5563",
            lineHeight: "1.8",
          }}
        >
          <li>
            Total Products:
            {" "}
            {summary.total_products}
          </li>

          <li>
            Total Customers:
            {" "}
            {summary.total_customers}
          </li>

          <li>
            Total Orders:
            {" "}
            {summary.total_orders}
          </li>

          <li>
            Products needing restock:
            {" "}
            {summary.low_stock_products}
          </li>
        </ul>

      </div>

    </div>
  );
}

export default Dashboard;