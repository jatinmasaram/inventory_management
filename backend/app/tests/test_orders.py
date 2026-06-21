import uuid


sku = str(uuid.uuid4())

def test_insufficient_stock(
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

    product = client.post(
        "/products",
        json={
            "name":
            "Limited Product",
            "sku":
            sku,
            "price":
            100,
            "stock_quantity":
            2,
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
            "Order User",
            "email":
            f"{uuid.uuid4()}@test.com",
            "phone":
            "9999999998",
        },
        headers=headers,
    )

    customer_id = (
        customer.json()["id"]
    )

    order = client.post(
        "/orders",
        json={
            "customer_id":
            customer_id,
            "items": [
                {
                    "product_id":
                    product_id,
                    "quantity":
                    50,
                }
            ],
        },
        headers=headers,
    )

    assert (
        order.status_code
        == 400
    )




def test_get_orders(client):

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

    response = client.get(
        "/orders",
        headers={
            "Authorization":
            f"Bearer {token}"
        },
    )

    assert (
        response.status_code
        == 200
    )