# czytanie z pliku (niewidzialne) r - read
# jesli plik nie istnieje, python zwroci nam błąd FileNotFoundError
with open('czytanie.txt') as fd:
    # zwraca całą zawrtość pliku
    fd.read()
    # zwraca pierwszą linijkę w pliku
    fd.readline()
    # zwraca liste wszystkich linijek w pliku
    fd.readlines()
    
# nadpisywanie pliku w - write
# w przypadku zapisu/nadpisu/dopisu jesli plik nie istnieje, zosatnie automatycznie stworzony
with open('nadpisywan.txt', 'w') as fd:
    # write - dopisz tekst typu string
    tekst = "Programowanie jest super"
    fd.write(tekst)
    
    # writelines - dopisz wszystkie elementy z podanej listy
    teksty = ['Python', 'Java', 'C++', 'JavaScript']
    fd.writelines(teksty)
    
# dopisywanie do pliku a - append
with open('dopisywanie.txt', 'a') as fd:
    tekst = "Programowanie jest super"
    fd.write(tekst)
    
    teksty = ['Python', 'Java', 'C++', 'JavaScript']
    fd.writelines(teksty)
    