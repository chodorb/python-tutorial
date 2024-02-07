# Napiszemy gre do nauki tabliczki mnozenia
# Program bedzie losowal 2 liczby i pytal o ich iloczyn
# jesli uzytkownik odpowie bezblednie, naliczy mu sie punkt
# po zakonczonej grze, ilosc punktow zapisze sie do pliku wyniki.txt
# na koncu poinformujemy uzytkownika, ktore ma miejsce w tabeli
import random

name = input("Wprowadz swoje imie: ")
score = 0

while True:
    a = random.randint(1,12)
    b = random.randint(1,12)
    
    answer = int(input(f"{a} x {b} = ? "))
    
    if a * b == answer:
        score += 10
    else:
        break

with open('wyniki.txt') as fd:
    lines = fd.readlines()
    
highscore = True
    
for line in lines:
    line = line.strip()
    line_score = int(line.split(' ')[1]) # Konwertujemy do inta 2 element po spacji czyli wynik gracza np. Bazyli 10
    if score <= line_score:
        highscore = False
        
if highscore:
    print("Ustanowiłeś nowy rekord, brawo !")
    
with open('wyniki.txt', 'a') as fd:
    fd.write(f"{name} {score}\n")