backend/app

├── api
│   ├── products.py
│   ├── customers.py
│   ├── orders.py
│   └── dashboard.py
│
├── core
│   ├── config.py
│   ├── logger.py
│   ├── exceptions.py
│   └── security.py
│
├── db
│   ├── base.py
│   ├── session.py
│   └── init_db.py
│
├── middleware
│   ├── request_id.py
│   ├── logging_middleware.py
│   └── rate_limiter.py
│
├── models
│   ├── product.py
│   ├── customer.py
│   ├── order.py
│   ├── order_item.py
│   └── inventory_audit.py
│
├── repositories
│   ├── product_repository.py
│   ├── customer_repository.py
│   ├── order_repository.py
│   └── inventory_repository.py
│
├── schemas
│   ├── product.py
│   ├── customer.py
│   ├── order.py
│   └── common.py
│
├── services
│   ├── product_service.py
│   ├── customer_service.py
│   ├── order_service.py
│   └── inventory_service.py
│
├── tests
│
├── utils
│   ├── constants.py
│   └── helpers.py
│
└── main.py
Phase 2 — Config Management

Everything from environment variables.

Never hardcode.

.env
APP_NAME=Inventory System

API_PREFIX=/api/v1

DEBUG=True

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=inventory_db
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

DATABASE_URL=postgresql+psycopg://postgres:postgres@postgres:5432/inventory_db

REDIS_HOST=redis
REDIS_PORT=6379

REDIS_URL=redis://redis:6379

RATE_LIMIT=100

LOG_LEVEL=INFO
core/config.py

Use:

pydantic-settings

Not:

os.getenv()

everywhere.

Single source of truth.

from pydantic_settings import BaseSettings

Real production pattern.

Phase 3 — Logging

This is where projects start looking serious.

logger.py

Create structured logging.

Example:

{
  "timestamp":"...",
  "request_id":"123",
  "method":"POST",
  "path":"/orders",
  "status":201
}

Every request logged.

Every exception logged.

Every stock change logged.

Phase 4 — Request ID Middleware

Generate:

X-Request-ID

for every request.

Store:

uuid.uuid4()

Why?

Production debugging.

Phase 5 — Global Exception Handling

Create:

core/exceptions.py

Custom exceptions:

ProductNotFoundException

CustomerNotFoundException

DuplicateSKUException

DuplicateEmailException

InsufficientStockException

Then:

@app.exception_handler(...)

Return consistent responses.

Example:

{
  "success": false,
  "message": "Insufficient stock",
  "request_id": "..."
}

instead of ugly FastAPI tracebacks.

Phase 6 — Database Models

Need 5 tables.

Product
id
name
sku
price
stock_quantity
created_at
updated_at
Customer
id
full_name
email
phone
created_at
Order
id
customer_id
total_amount
status
created_at
OrderItem
id
order_id
product_id
quantity
price_at_purchase
subtotal
InventoryAudit
id
product_id
old_stock
new_stock
reason
created_at

This is the production feature most people miss.

Phase 7 — Order Creation Transaction

Most important code in entire project.

Inside:

order_service.py

Flow:

BEGIN TRANSACTION

LOCK PRODUCT

VALIDATE STOCK

CREATE ORDER

CREATE ORDER ITEMS

REDUCE STOCK

INSERT AUDIT LOG

COMMIT

Use:

with db.begin():

and

with_for_update()

to lock rows.

This is what prevents overselling.

Phase 8 — Redis
Cache

Cache:

GET /products

TTL:

300 seconds

Invalidate on:

Create Product
Update Product
Delete Product
Rate Limiting

Middleware:

100 requests/minute/IP

Redis key:

rate_limit:127.0.0.1

Return:

429

if exceeded.

Phase 9 — Testing

Create:

test_product.py

test_customer.py

test_order.py

Must test:

Create Product

Duplicate SKU

Create Customer

Duplicate Email

Create Order

Inventory Reduction

Insufficient Stock

Rate Limiter
Phase 10 — Alembic

Never:

Base.metadata.create_all()

in production.

Use:

alembic revision --autogenerate
alembic upgrade head

Database version controlled.

First Actual Coding Order

Don't start with APIs.

Build in this order:

1. config.py
2. logger.py
3. db/session.py
4. db/base.py
5. models/
6. alembic
7. schemas/
8. repositories/
9. services/
10. middleware/
11. api/
12. tests/
13. docker
14. frontend

If you start with APIs first, you'll rewrite everything later.  


Data Integrity
No duplicate SKU
No duplicate Email
No negative inventory
No overselling
Transaction Safety
Order Created

AND

Inventory Reduced

OR

Nothing Happens

Never half-complete operations.

Concurrency Safety

Two users buying same product:

Stock = 5

User A buys 4
User B buys 4

System should not break.

Use:

SELECT ... FOR UPDATE
Observability

Logs.

Example:

{
  "request_id":"123",
  "endpoint":"/orders",
  "status":201
}

When production breaks:

Logs tell story.
Security
Rate Limiting
Input Validation
Environment Variables

No secrets in code.

Testing

A real engineer never says:

Works on my machine.

A real engineer says:

Tests passed.
What Will Impress Reviewers

Imagine reviewer sees:

FastAPI
React
Postgres

Normal.

Then sees:

Redis Rate Limiting

Redis Cache

Alembic Migrations

Pytest

Repository Pattern

Service Layer

Transaction Management

FOR UPDATE Locking

Docker Compose

Structured Logging

Now reviewer thinks:

This person understands backend engineering.
The Secret Weapon

Most candidates will focus on frontend.

You should focus on:

Order Service
Inventory Service
Database Consistency

because that's where engineering happens.





##ARCHITECTURE 
tep 1: Understand Business Domain

First question:

What is the most critical business operation?

For this project:

Order Creation

Because:

Products = CRUD

Customers = CRUD

Orders = BUSINESS LOGIC

If order creation is wrong:

Inventory wrong
Revenue wrong
Data wrong

Project fails.

Step 2: Design Database First

Before writing API.

Draw:

Customer

 1
 |
 *
Order

 1
 |
 *
OrderItem

 *
 |
 1

Product

Then:

Product
Customer
Order
OrderItem
InventoryAudit

Create ERD.

A senior spends more time here than coding.

Step 3: Define Data Constraints

Ask:

What can NEVER happen?

Examples:

Duplicate SKU
Duplicate Email
Negative Stock
Order Without Customer
Order Without Product

Put these in database.

Not just API.

Example:

UNIQUE(email)

UNIQUE(sku)

CHECK(stock_quantity >= 0)

Database becomes your last line of defense.

Step 4: Define Order Flow

Before code.

Literally write:

Create Order

↓

Validate Customer

↓

Validate Product

↓

Lock Product

↓

Check Stock

↓

Calculate Total

↓

Create Order

↓

Create Order Items

↓

Reduce Stock

↓

Create Audit Log

↓

Commit

Now implementation becomes easy.

Step 5: Decide Architecture

Before writing files.

For example:

API

↓

Service

↓

Repository

↓

Database

Rule:

API NEVER talks to DB directly
Step 6: Config

First code written.

Create:

.env

core/config.py

Why?

Every other file depends on it.

Step 7: Database Layer

Create:

db/base.py

db/session.py

Test connection.

No models yet.

Step 8: Models

Create:

Product

Customer

Order

OrderItem

InventoryAudit

Only models.

No API.

No services.

Step 9: Migrations

Setup:

alembic init alembic

Generate:

alembic revision --autogenerate

Run:

alembic upgrade head

Verify tables.

Step 10: Repository Layer

Example:

ProductRepository

CustomerRepository

OrderRepository

Only database operations.

Nothing else.

Step 11: Service Layer

This is where engineering happens.

Example:

OrderService

Contains:

Transactions

Inventory Checks

Stock Reduction

Audit Logs
Step 12: Tests Before APIs

Many people skip this.

Create:

test_order_service.py

Test:

Stock reduction

Insufficient stock

Order creation

If tests pass:

API becomes easy.

Step 13: Build APIs

Only now.

POST /products

POST /customers

POST /orders

Controllers become thin.

Step 14: Middleware

Add:

Logging

Request ID

Rate Limiting
Step 15: Redis

Add:

Product Cache

Rate Limiting
Step 16: Docker

After application works locally.

Never before.

Step 17: Frontend

Last.

Because frontend depends on API contracts.