# odczytaj dane z pliku client_data.csv
# wylosuj zwycięzce
import os
import csv
import random

file_path = "client_data.csv"

if os.path.exists(file_path):
    with open(file_path) as fd:
        reader = csv.reader(fd)
        clients = []
        for line in reader:
            clients.append(line)
    max_id = len(clients) - 1
    
    random_id = random.randint(1, max_id)
    winner = clients[random_id]
    
    print(f"Gratulacje {winner[1]}! Wygrałeś nagrode w naszym konkursie!")
    
else:
    print("Plik nie istnieje")