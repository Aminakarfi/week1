class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking' 

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        this_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight 

        if this_power > other_power:
            return f'{self.name} won the fight'
        elif this_power < other_power:
            return f'{other_dog.name} won the fight'  
        else:
            return "It's a tie"


Rex = Dog("Rex", 5, 4)
Body = Dog("Body", 8, 6)

print(Rex.bark())        
print(Rex.run_speed())   
print(Rex.fight(Body))    