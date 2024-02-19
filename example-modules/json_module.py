# tworzymy klase
# parsujemy dane z plik .json do naszej klasy
import json
import os


class Vehicle:
    def __init__(self, make, model, year, color, price, transmission, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.transmission = transmission
        self.mileage = mileage
    
    def __repr__(self):
        return self.make+self.model
    
    def is_taxed(self):
        if self.mileage >= 20000:
            return True
        return False
    
def get_vehicles(file_path):

    if os.path.exists(file_path):
        vehicles = []
        with open(file_path) as fd:
            json_data = json.load(fd)
            
        for vehicle in json_data['vehicles']:
            vehicle_object = Vehicle(
                make = vehicle['make'],
                model = vehicle['model'],
                year = vehicle['year'],
                color = vehicle['color'],
                price = vehicle['price'],
                transmission = vehicle['transmission'],
                mileage = vehicle['mileage']
            )
            vehicles.append(vehicle_object)
        
        return vehicles
    else:
        return None

vehicles = get_vehicles('vehices.json')
if vehicles:
    for vehicle in vehicles:
        print(vehicle.is_taxed())
else:
    print("File doesn't exist")