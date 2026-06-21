def test_login(client):

    response = client.post(
        "/auth/login",
        json={
            "email":
            "admin@example.com",
            "password":
            "admin123",
        },
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        "access_token"
        in response.json()
    )