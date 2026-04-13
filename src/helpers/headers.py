import os
from dotenv import load_dotenv

def post_request_headers():
        headers = {
            'Content-Type': 'application/json'
        }
        return headers


def get_request_headers():
    load_dotenv()
    headers = {
        'x-api-key': os.getenv('API_KEY')
    }
    return headers

def put_request_headers():
    headers = {
        'Content-Type': 'application/json'
    }
    return headers

def patch_request_headers():
    headers = {
        'Content-Type': 'application/json'
    }
    return headers

def login_existing_and_register_new_user_headers():
    load_dotenv()
    headers = {
        'x-api-key': os.getenv('API_KEY'),
        'Content-Type': 'application/json'

    }
    return headers

