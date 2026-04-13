

def create_object_payload():
        payload = {
                 "name": "Apple MacBook Pro 16",
                 "data": {
                    "year": 2026,
                    "price": 1849.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB NVmeSSD"
                    }
        }
        return payload


def update_object_payload():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2020,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    return payload

def partial_update_object_payload():
    payload = {
                "name": "Xiaomi MacBook Pro 16 (Updated Name)"
    }
    return payload





