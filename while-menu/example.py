# 1 - petla while True
# 2 - wypisz opcje dostepne dla user
# 3 - Pobierz opcje wybrana dla usera
# 4 - przypisz dzialania do opcji przez if/elif
# 5 - by zakonczyc dzilanie zrob break
# 6 - po else: wyswietl info ze nie ma takiej komendy


while True:
    """
    tu 
    wyswietl 
    opcje
    """
    
    command = input("Insert command: ")
    
    if command == "jakas wartosc":
        pass
    elif command == "jakas inna wartosc":
        pass
    elif command == "X":
        break
    else:
        print("Command not found")