# Retrieves detailed information for a single object specified by its unique ID.

import requests
from src.constants.api_url import api_url

class TestSingleObject(object):

    def test_single_object(self):
        url = api_url()
        end_point = url + '/ff8081819d62221a019d7d1ba3a922a1'
        response = requests.get(end_point)
        print(response.json())
        assert response.status_code == 200
