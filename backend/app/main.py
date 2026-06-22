from fastapi import FastAPI

from app.core.config import settings
from app.api.test import (
    router as test_router,
)

from app.core.exception_handlers import (
    register_exception_handlers,
)
from app.middleware.logging_middleware import (
    LoggingMiddleware,
)
from app.middleware.request_id import (
    RequestIDMiddleware,
)
from app.api.products import router as product_router
from app.api.customers import router as customer_router
from app.api.orders import router as order_router
from app.api.dashboard import router as dashboard_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import (
    router as auth_router,
)

app = FastAPI(
    title=settings.APP_NAME
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://inventory-management-j6tiffynq-jatinmasarams-projects.vercel.app",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(
    app
)

app.add_middleware(
    LoggingMiddleware
)

app.add_middleware(
    RequestIDMiddleware
)

app.include_router(
    product_router
)

app.include_router(
    customer_router
)
app.include_router(
    order_router
)
app.include_router(
    dashboard_router
)
app.include_router(
    auth_router
)
app.include_router(
    test_router
)

@app.get("/")
def root():
    return {
        "app": settings.APP_NAME,
        "status": "running",
    }

