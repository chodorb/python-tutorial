class Client:
    
    def __init__(self, name, last_name, age, gender, hobby, is_premium):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.hobby = hobby
        self.is_premium = is_premium
        
    def przedstaw_sie(self):
        print(f"Hej mam na imie {self.name}")
    
    def suggest_product(self):
        if self.gender == 'male':
            if self.age >= 18:
                return f"Polecamy dla ciebie bilet na wyscig samochodowy, co o tym mylisz {self.name}"
            elif self.age < 18:
                return f"Polecamy dla ciebie resoraki, brzmi fajnie prawda {self.name}?"
        elif self.gender == 'female':
            if self.age >= 18:
                return f"Polecamy dla ciebie bilet na koncert, co o tym mylisz {self.name}"
            elif self.age < 18:
                return f"Polecamy dla ciebie lalki, brzmi fajnie prawda {self.name}?"
