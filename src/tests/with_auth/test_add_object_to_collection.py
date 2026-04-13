import requests
import pytest

from src.constants.api_url import ApiUrl
from src.helpers.headers import login_existing_and_register_new_user_headers
from src.helpers.payload_manager import create_object_payload

class TestAddObjectToCollection:
    def test_add_object_to_collection(self):
        payload = create_object_payload()
        url = ApiUrl().collection_url() + '/laptops/objects'
        print(url)
        headers = login_existing_and_register_new_user_headers()

        response = requests.post(url, json=payload, headers=headers)
        assert response.status_code == 200

        print(response.text)