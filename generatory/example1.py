# napisz funkcje która wylosuje 100 cyfr od 1 - 25 i jeśli będzie wśród nich 6, to uytkownik wygrał B)
import random 

def generate_numbers(max):
    for _ in range(0,max):
        print("Generating ...")
        yield random.randint(1,25)
    
for num in generate_numbers(20):
    if num == 6:
        print("U won :)")
        break