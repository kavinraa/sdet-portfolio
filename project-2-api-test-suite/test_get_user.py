
def test_get_user_returns_correct_id(client):
    response = client.get_user(2)
    assert response.status_code == 200
    body = response.json()
    assert body ["data"]["id"] == 2
    