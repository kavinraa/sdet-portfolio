
def test_create_user_returns_201(client):
    response = client.create_user({"name" : "Bruce Wayne" , "alter ego" : "Batman" })
    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Bruce Wayne"
    assert body["alter ego"] == "Batman"
    assert "id" in body
    assert "createdAt" in body