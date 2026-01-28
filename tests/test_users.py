def test_get_users_returns_list(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
