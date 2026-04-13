import requests

from src.constants.api_url import api_url

class TestDeleteObject(object):
    def test_delete_object(self):
        url = api_url() + '/ff8081819d62221a019d7d262f0022a7'
        print(url)
        response = requests.delete(url)
        assert response.status_code == 200
        print(response.text)