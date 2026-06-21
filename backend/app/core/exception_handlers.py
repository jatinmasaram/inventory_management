from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    ProductNotFoundException,
    CustomerNotFoundException,
    OrderNotFoundException,
    DuplicateSKUException,
    DuplicateEmailException,
    InsufficientStockException,
    UnauthorizedException
)



def register_exception_handlers(
    app: FastAPI,
):

    @app.exception_handler(
        ProductNotFoundException
    )
    async def product_not_found_handler(
        request: Request,
        exc: ProductNotFoundException,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(
        CustomerNotFoundException
    )
    async def customer_not_found_handler(
        request: Request,
        exc: CustomerNotFoundException,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(
        OrderNotFoundException
    )
    async def order_not_found_handler(
        request: Request,
        exc: OrderNotFoundException,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(
        DuplicateSKUException
    )
    async def duplicate_sku_handler(
        request: Request,
        exc: DuplicateSKUException,
    ):
        return JSONResponse(
            status_code=409,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(
        DuplicateEmailException
    )
    async def duplicate_email_handler(
        request: Request,
        exc: DuplicateEmailException,
    ):
        return JSONResponse(
            status_code=409,
            content={
                "success": False,
                "message": str(exc),
            },
        )
    
    @app.exception_handler(
    UnauthorizedException
)
    async def unauthorized_handler(
        request,
        exc,
    ):

        return JSONResponse(
            status_code=401,
            content={
                "detail": str(exc)
            },
        )

    @app.exception_handler(
        InsufficientStockException
    )
    async def insufficient_stock_handler(
        request: Request,
        exc: InsufficientStockException,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": str(exc),
            },
        )