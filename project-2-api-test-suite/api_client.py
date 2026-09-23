import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.get(url)
        return response

    def create_user(self, user_data):
        url = f"{self.base_url}/users"
        response = requests.post(url, json = user_data)
        return response

    def update_user(self, user_id , user_data):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.put(url, json = user_data)
        return response

    def delete_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.delete(url)
        return response



# client = APIClient("https://reqres.in/api")
# result = client.create_user({"name" : "Morpheus" , "job" : "leader"})
# print(result.json())
# print(result.status_code)

# result = client.get_user(2)
# print(result.json()["data"]["id"])