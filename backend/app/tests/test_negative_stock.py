def test_negative_stock(
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

    response = client.post(
        "/products",
        json={
            "name":
            "Bad Product",
            "sku":
            "NEG-001",
            "price":
            50,
            "stock_quantity":
            -10,
        },
        headers=headers,
    )

    assert (
        response.status_code
        in [400, 422]
    )