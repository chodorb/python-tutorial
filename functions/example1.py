# wzor na pole koła
# wzor na delte
# wzor na pole prostokąta
from math import pi


def pole_prostokata(a, b):
    return a * b
    
def pole_kola(r):
    pole = pi * r**2
    return pole
    
def delta(a, b, c):
    delta = (b**2) - (4*a*c)
    return delta

def pole_kwadratu(a):
    print(a*a)

pole_p = pole_prostokata(29,321)
pole_k = pole_kola(16)
wynik_delta = delta(3,5,7)
pole_kw = pole_kwadratu(5) # None

print(f"Pole prostokata wynosi {pole_p}")
print(f"Pole koła wynosi {pole_k}")
print(f"Delta wynosi {wynik_delta}")
print(f"Pole kwadratu wynosi {pole_kw}")
