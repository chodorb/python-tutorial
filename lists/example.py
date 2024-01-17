# 1 - Add stuff to the list
# 2 - Remove stuff from the list
# 3 - Edit stuff in the list
# 4 - For loop through the list
# 5 - Display stuff at given list index

# lista przechowuje wiele wartosci, aby skorzystac z konkretnej skorzystaj z indeksu
# np lista[0] -> John

lista = ["John", "Alice", "Bob", "George"]

# Takie menu z while oraz if/elif/else będzie się powtarzać cały kurs
while True:
    print("1 - Add stuff to the list")
    print("2 - Remove stuff from the list")
    print("3 - Edit stuff in the list")
    print("4 - For loop through the list")
    print("5 - Display stuff at given list index")
    print("X - exit")
    
    command = input("Insert command: \n")
    
    if command == "1":
        new_element = input("Insert new element: ")
        lista.append(new_element)
    elif command == "2":
        element_to_delete = input("Delete element: ")
        
        # czy element który chcemy wywalić jest w liscie
        if element_to_delete in lista:
            lista.remove(element_to_delete)
        else:
            print("No such element to delete")
    elif command == "3":
        index = int(input("Insert index: "))
        new_element_value = input("Insert new element value: ")
        lista[index] = new_element_value
    elif command == "4":
        for element in lista:
            print(element)
    elif command == "5":
        index = int(input("Insert index: "))
        print(lista[index])
    elif command == "X":
        break
    else: 
        print("Command not found")
        
    print(f"Our list: {lista}")