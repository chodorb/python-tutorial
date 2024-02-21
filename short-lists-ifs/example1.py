name = input("name: ")

# <<przypisanie jesli warunek jest spelniony>> if <<warunek>> else <<przypisanie jesli warunek nie jest spelniony>>

# if name:
#     name = name.capitalize()
    
# else:
#     name = "my friend"

name = name.capitalize() if name else "my friend"

print(f"Hello {name}!")