#Retrieves a list of all available collections with basic metadata.
# Each collection represents a logical grouping of objects (for example, phones, computers, etc.).

import requests

from src.constants.api_url import collection_url

class TestListAllCollection:
    def test_list_all_collection(self):

        url = collection_url()
        headers = {
            # 'Content-Type': 'application/json',
            'x-api-key': '0f49f5c8-b745-43bd-9612-000801867758'
        }

        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        print(response)

