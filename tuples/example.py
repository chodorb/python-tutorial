# 1 - For loop through the tuple
# 2 - Display element at given index

# tuple są nieedytowalne (immutatble)
example_tuple = ("Bazyli", "Marcin", "Kasia") # len -> 3 max_index -> 2


while True:
    print("1 - For loop through the tuple")
    print("2 - Display element at given index")
    print("X - exit")
    
    command = input("Insert command: ")
    
    if command == "1":
        for element in example_tuple:
            print(element)
    elif command == "2":
        index = int(input("Insert index: "))
        
        # ten if sprawdza nam czy index miesci sie w tuplu/liscie
        if len(example_tuple) < index + 1:
            print("Index out of range")
        else:
            print(example_tuple[index])    
    elif command == "X":
        break
    else: 
        print("Command not found")