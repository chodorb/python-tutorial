# Program obliczający BMI użytkownika
print("Witaj w programi obliczającym BMI.")

gender = input("K / M: \n")
weight = float(input("Podaj swoją masę: \n"))
height = int(input("Podaj swój wzrost: \n"))

bmi = round(weight / (height ** 2) * 10000, 2)

if bmi > 25:
    print("Twoja waga jest zbyt duża. Rozważ zdrowszy tryb życia.")
    if gender == "M":
        print("Mamy dla ciebie ofertę kursu treningowego autorstwa Roberta Lewandowskiego!")
    elif gender == "K":
        print("Zakup plan treningowy, od Ewy Chodakowskiej!")
    else:
        print("Niewłaściwe wprowadzono płeć.")
elif bmi < 25 and bmi > 18.5:
    print("Twoja waga jest optymalna. Tak trzymaj.")
elif bmi < 18.5:
    print("Twoja waga powinna być wyższa. Rozważ lepsze odżywianie.")
    if gender == "M":
        print("Zamów, przepyszny catering marki MANPLUS!")
    elif gender == "K":
        print("Zamów catering od Anny Lewandowskiej!")
    else:
        print("Niewłaściwe wprowadzono płeć.")
