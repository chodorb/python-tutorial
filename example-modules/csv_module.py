import csv
import os

file_path = "client_data.csv"

if os.path.exists(file_path):
    with open(file_path) as fd:
        reader = csv.reader(fd)
        for line in reader:
            print(line)
            # spróbuj wykonać linjki pod try
            try:
                last_id = int(line[0])
            # ignoruj błędy ValueError
            except ValueError:
                continue
    
    with open(file_path, 'a') as fd:
        first_name = input("first name: ")
        last_name = input("last name: ")
        email = input("email: ")
        phone = input("phone: ")
        city = input("city: ")
        country = input("country")
        
        writer = csv.writer(fd)
        writer.writerow([last_id+1, first_name, last_name, email, phone, city, country])