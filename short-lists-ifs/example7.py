# z listy z imionami, wyciagnij imiona meskie

names = ['bazyli', 'kinga', 'albert', 'krystyna', 'adrian']

# nowa_tablica = [ <<nowy_element>> for <<element>> in <<lista>> if <<warunek z udziałem elementu>>]
# krok 1 - "przepisz" pętle
# krok 2 - "przepisz" zawartosc append
# krok 3 - "przepisz" warunek
# python string slices

male_names = [name.capitalize() for name in names if name[-1] != 'a' ]

female_names = [name.capitalize() for name in names if name[-1] == 'a' ]

print(male_names)
print(female_names)