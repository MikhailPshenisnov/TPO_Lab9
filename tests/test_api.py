import requests

BASE_URL = "https://reqres.in/api"

HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": "reqres-free-v1"
}


class TestReqresAPI:
    def test_get_user(self):
        response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)

        assert response.status_code == 200

        json_data = response.json()["data"]

        assert json_data["id"] == 2
        assert json_data["email"] == "janet.weaver@reqres.in"
        assert "first_name" in json_data
        assert response.elapsed.total_seconds() < 1.0

    def test_create_user(self):
        payload = {
            "name": "John Doe",
            "job": "QA Engineer"
        }

        response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)

        assert response.status_code == 201

        json_data = response.json()

        assert json_data["name"] == "John Doe"
        assert json_data["job"] == "QA Engineer"
        assert "id" in json_data
        assert "createdAt" in json_data

    def test_update_user(self):
        payload = {
            "name": "John Updated",
            "job": "Senior QA"
        }

        response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)

        assert response.status_code == 200

        json_data = response.json()

        assert json_data["name"] == "John Updated"
        assert json_data["job"] == "Senior QA"
        assert "updatedAt" in json_data
