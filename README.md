# Inventory Management System

Production-ready full-stack Inventory & Order Management System built using FastAPI, React, PostgreSQL, Docker, and Docker Compose.

## Overview

This application enables businesses to manage:

* Products
* Customers
* Orders
* Inventory Tracking

The system automatically validates inventory, prevents overselling, tracks stock movements, and provides business insights through a dashboard.

---

## Architecture

The backend follows a layered architecture:

```text
API Layer
    ↓
Service Layer
    ↓
Repository Layer
    ↓
PostgreSQL
```

### Design Principles

* Separation of Concerns
* Repository Pattern
* Service Layer Pattern
* Dependency Injection
* Centralized Exception Handling
* JWT Authentication
* Containerized Deployment

---

## Features

### Product Management

* Create Product
* View Products
* Update Product
* Delete Product
* Unique SKU Validation

### Customer Management

* Create Customer
* View Customers
* Delete Customer
* Unique Email Validation

### Order Management

* Create Orders
* View Orders
* Delete Orders
* Automatic Order Total Calculation
* Inventory Validation

### Inventory Tracking

* Automatic Stock Reduction
* Inventory Audit Logs
* Low Stock Monitoring
* Negative Inventory Prevention

### Dashboard

* Total Products
* Total Customers
* Total Orders
* Low Stock Products

---

## Security Features

### JWT Authentication

* Secure Login
* Protected API Endpoints
* Role-Based Access Control (RBAC)

### Password Security

* BCrypt Password Hashing
* Password Verification

---

## Reliability Features

### Database Transaction Safety

To prevent concurrent inventory issues, product rows are locked during order creation using:

```python
.with_for_update()
```

This ensures inventory consistency and prevents overselling.

### Centralized Error Handling

Custom exceptions:

* ProductNotFoundException
* CustomerNotFoundException
* OrderNotFoundException
* DuplicateSKUException
* DuplicateEmailException
* InsufficientStockException
* UnauthorizedException

---

## Observability

### Request Logging

Custom middleware logs:

* HTTP Method
* Endpoint
* Status Code
* Processing Time

### Request Correlation

Every request receives a unique Request ID for easier debugging and tracing.

---

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL
* JWT
* BCrypt
* Redis

### Frontend

* React
* React Router
* Axios
* Vite

### Infrastructure

* Docker
* Docker Compose

---

## Containerized Architecture

Services:

* Frontend Container
* Backend Container
* PostgreSQL Container
* Redis Container

Persistent database storage is provided using Docker named volumes.

---

## Running Locally

```bash
docker-compose up --build
```

Application URLs:

Frontend:
http://localhost:5173

Backend:
http://localhost:8000

Swagger:
http://localhost:8000/docs

---

## Future Improvements

* Refresh Tokens
* Redis Response Caching
* Rate Limiting
* API Versioning
* CI/CD Pipeline
* Kubernetes Deployment
* OpenTelemetry Observability
* Distributed Tracing

---

## Author

Jatin Masaram

Software Engineer
