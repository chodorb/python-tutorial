# 1 - Add stuff to the set
# 2 - Remove stuff from the set
# 3 - Edit stuff in the set
# 4 - For loop through the set

# set - zbiór
# list/array - lista/tablica
# tuple - krotka
# dict - słownik

# 1 - zbiory nie akceptują duplikatów
# 2 - zbiory nie maja indeksow bo sa loseowe

example_set = {"Bazyli", "Marcin", "Kasia", "Jagoda"}

while True:
    
    print(example_set)
    
    print("1 - Add stuff to the set")
    print("2 - Remove stuff from the set")
    print("3 - Edit stuff in the set")
    print("4 - For loop through the set")
    print("X - exit")
    
    command = input("Insert command")
    
    if command == "1":
        new_element = input("Insert new element: ")
        if new_element not in example_set:
            example_set.add(new_element)
        else:
            print("Element already in the set")
    elif command == "2":
        element_to_delete = input("Delete element: ")
        if element_to_delete in example_set:
            example_set.remove(element_to_delete)
        else:
            print("Element not in the set")
    elif command == "3":
        # Nie mozemy dostac sie do konkretnych wartosci, gdyz set nie posiada indexu (jest losowy)
        print("Not possible")
    elif command == "4":
        for element in example_set:
            print(element)
    elif command == "X":
        break
    else: 
        print("Command not found")