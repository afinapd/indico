import requests
from typing import Dict, Any

class PetApi:
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def add_new_pet(self, pet_data: Dict[str, Any]) -> requests.Response:
        """Add a new pet to the store"""
        endpoint = f"{self.base_url}/pet"
        response = requests.post(endpoint, json=pet_data, headers=self.headers)
        return response

    def find_pets_by_status(self, status: str) -> requests.Response:
        """Find pets by status"""
        endpoint = f"{self.base_url}/pet/findByStatus"
        params = {"status": status}
        response = requests.get(endpoint, params=params, headers=self.headers)
        return response
