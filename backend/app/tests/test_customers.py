def test_duplicate_email(
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
        "full_name":
        "Test User",
        "email":
        "duplicate@test.com",
        "phone":
        "9999999999",
    }

    client.post(
        "/customers",
        json=payload,
        headers=headers,
    )

    second = client.post(
        "/customers",
        json=payload,
        headers=headers,
    )

    assert (
        second.status_code
        == 409
    )



def test_get_customers(client):

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
        "/customers",
        headers={
            "Authorization":
            f"Bearer {token}"
        },
    )

    assert response.status_code == 200