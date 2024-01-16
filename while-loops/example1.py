# Imie
# Nazwisko
# Plec

while True:
    name = input("Jak masz na imie: \n")
    last_name = input("Jak masz na nazwisko: \n")
    gender = input("K/M (opcjonalne) : \n")

    if name:
        if last_name:
            if not gender or gender == "M" or gender == "K":
                break
            else:
                print("Niepoprawna plec")
        else:
            print("Nie wprowadzono nazwiska")
    else:
        print("Nie wprowadzono imienia")

if gender:
    print(f"{name} {last_name} -> {gender}")
else:
    print(f"{name} {last_name}")

