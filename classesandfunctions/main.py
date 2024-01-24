from utils import get_client_objects

client_objects = get_client_objects()

for client in client_objects:
    print(client.suggest_product())
