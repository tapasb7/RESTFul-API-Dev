# Authenticates an existing user using valid credentials.
# Upon successful login, this endpoint generates and returns a valid JSON Web Token (JWT)
# that can be used to authorize future requests to other endpoints.
# Many endpoints in this API optionally support authentication and can be accessed as protected endpoints
# by including the query parameter ?auth-type=jwt along with the JWT issued by this /login endpoint.

import requests
import pytest


from src.constants.api_url import ApiUrl
from src.helpers.headers import login_existing_and_register_new_user_headers
from src.helpers.payload_manager import login_existing_user_payload

class TestLoginExistingUser:
    @pytest.mark.smoketest
    def test_login_existing_user(self):
        url = ApiUrl().login_existing_user()
        headers = login_existing_and_register_new_user_headers()
        payload = login_existing_user_payload()
        print(payload)
        print(headers)
        print(url)

        response = requests.post(url, headers=headers, json=payload)
        print(response.text)
        assert response.status_code == 200
        assert response.status_code != 401

        print(response.raise_for_status())
        print('Token : ',response.json().get('token'))
        print('Token Type : ',response.json().get('tokenType'))



