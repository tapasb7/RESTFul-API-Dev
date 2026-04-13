#Retrieves a list of all available collections with basic metadata.
# Each collection represents a logical grouping of objects (for example, phones, computers, etc.).

import requests

from src.constants.api_url import ApiUrl
from src.helpers.headers import get_request_headers

class TestListAllCollection:
    def test_list_all_collection(self):

        url = ApiUrl().collection_url()
        headers = get_request_headers()

        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        print(response.json(), end='')


