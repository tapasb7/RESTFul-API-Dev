import pytest
import requests

from src.constants.api_url import ApiUrl
from src.helpers.headers import post_request_headers
from src.helpers.headers import login_existing_and_register_new_user_headers
from src.helpers.payload_manager import login_existing_user_payload
from src.helpers.payload_manager import create_object_payload

@pytest.fixture
def get_object_id():
    url = ApiUrl.api_url()
    headers = post_request_headers()
    payload = create_object_payload()
    response = requests.post(url=url, headers=headers, json=payload)
    response_data = response.json()
    object_id = response_data.get('id')
    return object_id


@pytest.fixture
def get_token():
    url = ApiUrl().login_existing_user()
    headers = login_existing_and_register_new_user_headers()
    payload = login_existing_user_payload()
    response = requests.post(url=url, headers=headers, json=payload)
    return response.json().get('token')


