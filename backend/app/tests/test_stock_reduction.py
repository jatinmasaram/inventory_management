import uuid


def test_stock_reduction(
    client
):

    response = client.post(
        "/auth/login",
        json={
            "email":
            "admin@example.com",
            "password":
            "admin123",
        },
    )

    token = response.json()[
        "access_token"
    ]

    headers = {
        "Authorization":
        f"Bearer {token}"
    }

    sku = str(
        uuid.uuid4()
    )

    product = client.post(
        "/products",
        json={
            "name":
            "Stock Product",
            "sku":
            sku,
            "price":
            100,
            "stock_quantity":
            10,
        },
        headers=headers,
    )

    product_id = (
        product.json()["id"]
    )

    customer = client.post(
        "/customers",
        json={
            "full_name":
            "Stock User",
            "email":
            f"{uuid.uuid4()}@test.com",
            "phone":
            "9999999997",
        },
        headers=headers,
    )

    customer_id = (
        customer.json()["id"]
    )

    client.post(
        "/orders",
        json={
            "customer_id":
            customer_id,
            "items": [
                {
                    "product_id":
                    product_id,
                    "quantity":
                    2,
                }
            ],
        },
        headers=headers,
    )

    updated_product = client.get(
        f"/products/{product_id}",
        headers=headers,
    )

    assert (
        updated_product
        .json()["stock_quantity"]
        == 8
    )