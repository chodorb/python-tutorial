# 1 - Add stuff to the dict
# 2 - Remove stuff from the dict
# 3 - Edit stuff in the dict
# 4 - For loop through the dict

example_dict = {
    "name": "Bazyli",
    "last_name": "Chodor",
    "gender": "Male",
    "hobby": "Sport",
}

# W dict przechowywane sa pary klucz - wartosc
# klucze sa unikalne
# petla for przyjmuje 2 wartosci kiedy petlujemy sie przez dict.items()

# print(example_dict['name']) -> Bazyli

while True:
    
    print(example_dict)
    print("1 - Add stuff to the dict")
    print("2 - Remove stuff from the dict")
    print("3 - Edit stuff in the dict")
    print("4 - For loop through the dict")
    print("X - exit")
    
    command = input("Insert command: ")
    
    if command == "1":
        key = input("Insert key: ")
        if key in example_dict.keys():
            print("The key is already in the dict")
        else:
            value = input("Insert value: ")
            example_dict[key] = value
    elif command == "2":
        key = input("Insert key: ")
        if key in example_dict.keys():
            del example_dict[key]
        else:
            print("The key is not in the dict")
    elif command == "3":
        key = input("Insert key: ")
        if key in example_dict.keys():
            value = input("Insert value: ")
            example_dict[key] = value
        else:
            print("This key is not in the dict")
            
    elif command == "4":
        for key, value in example_dict.items():
            print(f"key: {key}, value: {value}")
            
    elif command == "X":
        break
    else:
        print("Command not found")