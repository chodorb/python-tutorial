# Użytkownik wprowadza liczbe graczy
# Program dla każdego gracza losuje czy piją shota
from random import randint

print("Witaj w naszej grze!")
number_of_players = int(input("Wprowadz liczbe graczy: \n"))

for player in range(number_of_players):
    result = randint(1,2)
    if result == 1:
        print(f"Gracz numer: {player + 1} pije wode. Uffff")
    else:
        print(f"Gracz numer: {player + 1} trafił na wódkę. Ale pech")