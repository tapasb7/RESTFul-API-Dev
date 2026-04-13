# Completely replaces the data of an existing object identified by its ID with new information.

import json
import requests

from src.constants.api_url import api_url
from src.helpers.payload_manager import update_object_payload
from src.helpers.headers import put_request_headers

class TestUpdateObject(object):
    def test_update_object(self):
        end_point = '/ff8081819d62221a019d7d0acff92291'
        url = api_url() + end_point
        print(url)
        headers = put_request_headers()
        print(headers)
        payload = update_object_payload()
        print(payload)

        response = requests.put(url, headers=headers, json=payload)
        assert response.status_code == 200

        with open(r'C:\Users\user\PycharmProjects\PyATB5xLearning\restful_api_dev\updated_object.json', 'w') as outfile:
            json.dump(response.json(), outfile, indent=4)

