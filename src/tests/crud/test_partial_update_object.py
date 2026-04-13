# Applies partial modifications to an object by updating only specific fields provided in the request body.

import json
import requests

from src.constants.api_url import api_url
from src.helpers.payload_manager import partial_update_object_payload
from src.helpers.headers import patch_request_headers

class TestUpdateObject(object):
    def test_update_object(self):
        end_point = '/ff8081819d62221a019d7d21820f22a3'
        url = api_url() + end_point
        headers = patch_request_headers()
        payload = partial_update_object_payload()

        response = requests.patch(url, headers=headers, json=payload)
        assert response.status_code == 200
        print(response.json())

        with open(r'C:\Users\user\PycharmProjects\PyATB5xLearning\restful_api_dev\partial_updated_object.json', 'w') as outfile:
            json.dump(response.json(), outfile, indent=4)

