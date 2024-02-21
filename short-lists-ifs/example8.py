results = [90, 47, 36, 74, 20, 15, 100]
# EGZAMIN ZDAWALNY OD 50%

# nowa_tablica = [ <<nowy_element>> for <<element>> in <<lista>> if <<warunek z udziałem elementu>>]
# krok 1 - "przepisz" pętle
# krok 2 - "przepisz" zawartosc append
# krok 3 - "przepisz" warunek

OK_results = [result for result in results if result >= 50]

print(OK_results)