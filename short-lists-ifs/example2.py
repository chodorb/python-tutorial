import random

random_number = random.randint(1, 100)

# <<przypisanie jesli warunek jest spelniony>> if <<warunek>> else <<przypisanie jesli warunek nie jest spelniony>>

# if random_number % 2 == 0:
#     information = "even"
# else:
#     information = "odd"

information = "even" if random_number % 2 ==0 else "odd"


    
print(f"The number {random_number} is {information}!")