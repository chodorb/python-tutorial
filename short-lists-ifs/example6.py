# wygeneruj parzyste liczby od 1 do 20



# nowa_tablica = [ <<nowy_element>> for <<element>> in <<lista>> if <<warunek z udziałem elementu>>]
# krok 1 - "przepisz" pętle
# krok 2 - "przepisz" zawartosc append
# krok 3 - "przepisz" warunek

# for x in range(1,21):
#     if x % 2 == 0:
#         evens.append(x)

evens = [x for x in range(1, 21) if x % 2 == 0]


        

print(evens)