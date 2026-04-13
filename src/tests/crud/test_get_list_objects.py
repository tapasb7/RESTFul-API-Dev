# List of all objects

import requests
import json

class TestListObjects:

    def test_list_objects(self):
        url = 'https://api.restful-api.dev/objects'
        response = requests.get(url=url)
        response_date = response.json()
        assert response.status_code == 200
        print(response.text)

        with open(r'C:\Users\user\PycharmProjects\PyATB5xLearning\restful_api_dev\objects_data.json', 'w') as file:
            json.dump(response_date, file, indent=4)

        for i in response_date:
            if 'Apple' in i['name']:
                print(i['name'])