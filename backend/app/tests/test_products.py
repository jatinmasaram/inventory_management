def test_duplicate_sku(
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

    payload = {
        "name":
        "Duplicate Product",
        "sku":
        "DUP-001",
        "price":
        100,
        "stock_quantity":
        20,
    }

    client.post(
        "/products",
        json=payload,
        headers=headers,
    )

    second = client.post(
        "/products",
        json=payload,
        headers=headers,
    )

    assert (
        second.status_code
        == 409
    )


def test_get_products(client):

    response = client.post(
        "/auth/login",
        json={
            "email": "admin@example.com",
            "password": "admin123",
        },
    )

    token = response.json()[
        "access_token"
    ]

    response = client.get(
        "/products",
        headers={
            "Authorization":
            f"Bearer {token}"
        },
    )

    assert response.status_code == 200