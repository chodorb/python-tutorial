# funkcje do tworzenia klas
from clients import Client
from client_data import client_data


def get_client_objects():
    client_objects = []
    for client in client_data:
        client_obj = Client(name=client['name'],
                            last_name=client['last_name'],
                            age=client['age'],
                            gender=client['gender'],
                            hobby=client['hobby'],
                            is_premium=client['is_premium'])
        client_objects.append(client_obj)
    
    return client_objects