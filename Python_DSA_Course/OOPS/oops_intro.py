class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_age(self): # an exmaple of getters
        return self.age
    
    def get_name(self): # an example of getters
        return self.name
    
    def set_age(self, age): # an example of setters
        self.age = age #used to modify/overwrite attributes defined in __init__

d = Dog("Victor", 23)
d1 = Dog("tim", 3)
print(d.get_name())
d.set_age(34)
print(d.get_age())

        