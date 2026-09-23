
def test_update_user_returns_200(client):
    response = client.update_user(2 , {"name" : "Bruce Wayne" , "quote" : "Never Give Up"})
    assert response.status_code == 200
    body = response.json()
    assert "updatedAt" in body
    assert body["name"] == "Bruce Wayne"
    assert body["quote"] == "Never Give Up"


def test_delete_user_returns_204(client):
    response = client.delete_user(2)
    assert response.status_code == 204
    

