# create classes that represent a dog and a cat

class Animal:
    def __init__(self, name, gender, breed, weight):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.weight = weight
        
    def pet(self):
        return f"{self.name} is happy :)"


class Dog(Animal):
    def __init__(self, name, gender, breed, weight, is_restricted):
        super().__init__(name, gender, breed, weight)
        # is the same as:
        # self.name = name
        # self.gender = gender
        # self.breed = breed
        # self.weight = weight
        self.is_restricted = is_restricted
    
    def speak(self):
        return f"Dog {self.name} said WOOF!"


class Cat(Animal):
    def speak(self):
        return f"Cat {self.name} said MEOW!"
    


class Hamster(Animal):
    
    def speak(self):
        return f"Hamster {self.name} said SQUEAK!"
    

cat1 = Cat(name="Filemon", gender="M", breed="Street Cat", weight=4.0)
dog1 = Dog(name="Reksio", gender="M", breed="Street Dog", weight=9.0, is_restricted=True)
hamster1 = Hamster(name="Alvin", gender="M", breed=None, weight=0.5)

print(cat1.speak())
print(dog1.speak())
print(hamster1.speak())