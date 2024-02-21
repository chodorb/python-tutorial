ceny_netto = [500, 1000, 1200, 430, 100] # * 0.77 = 1.00 - 0.23

# nowa_lista = [ <<nowy_element>> for <<element>> in <<lista>> ]
ceny_brutto = [ round(cena * 0.77, 2) for cena in ceny_netto ]

print("ceny netto " + str(ceny_netto))
print("ceny_brutto " + str(ceny_brutto))

print("zaplacony podatek: " + str(round(sum(ceny_netto) - sum(ceny_brutto), 2)))