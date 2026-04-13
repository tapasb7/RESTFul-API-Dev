# Creates and stores a new object using the data provided in the request body.

import requests
import json
import logging

from src.constants.api_url import api_url
from src.helpers.headers import post_request_headers
from src.helpers.payload_manager import create_object_payload

class TestCreateNewObjects:

    def test_create_new_objects(self):
        logger = logging.getLogger(__name__)
        url = api_url()
        headers = post_request_headers()
        payload = create_object_payload()
        logger.info('-----------------Staring Test------------------')
        logger.info('-----------------Creating post request------------------')

        response = requests.post(url=url, headers=headers, json=payload)
        logger.info('-----------------response text------------------')
        print('\n',response.text)

        assert(response.status_code == 200)
        response_data = response.json()
        print(response_data.get('id'))
        logger.info('-----------------assert test completed------------------')
        logger.info('-----------------write the new object response payload to JSON file------------------')

        with open(r'C:\Users\user\PycharmProjects\PyATB5xLearning\restful_api_dev\new_object.json', 'w') as file:
            json.dump(response_data, file, indent=4)





