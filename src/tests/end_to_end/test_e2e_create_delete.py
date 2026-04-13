import requests

from src.constants.api_url import put_patch_delete_url

class TestE2ECreateDeleteObject():
    def test_create_delete_object(self, get_object_id):
        object_id = get_object_id
        print('\n Created object with ID : ',object_id)
        url = put_patch_delete_url(self, object_id)
        print('\n URL : ',url)


        response = requests.delete(url)
        assert response.status_code == 200
        print('\n Deleted object with ID : ',object_id)
        print(response.text)

