# every employee has his account in the system
# the employee will be able to add hours to the system
# additionally managers will be able to view the hours summary in the system
class AccessDeniedError(Exception):
    pass


users = []

class User:
    def __init__(self, first_name, last_name, postion):
        self.first_name = first_name
        self.last_name = last_name
        self.position = postion
        self.hours = 0
        users.append(self)
        
    def add_hours(self, hours):
        self.hours += hours
        
    def say_hello(self):
        return f"hello {self.first_name}"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    

class EmployeeUser(User):
    def view_hour_summary(self):
        raise AccessDeniedError("You have no access rights to hour summary!")

class ManagerUser(User):
    def view_hour_summary(self):
        return [{"user":user, "hours": user.hours} for user in users]
    
employee1 = EmployeeUser("Bazyli", "Chodor", "Programista")
manager1 = ManagerUser("Michał", "S", "Manager")

employee1.add_hours(12)

manager1.add_hours(9)

print(manager1.view_hour_summary())
