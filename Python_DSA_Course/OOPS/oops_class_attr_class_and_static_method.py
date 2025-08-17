# Example of class attribute

class Person:
    number_of_people = 0 # class attribute: belongs to a class and not to a specific instance of it
    
    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("Logan")
print(p1.number_of_people) # or print(p2.number_of_people) or print(Person.number_of_people)
       
# Example of class method
        
class Animal:
    number_of_animals = 0 
    
    def __init__(self, name):
        self.name = name
        Animal.add_animal()
        
    @classmethod
    def number_of_animal(cls): # this method is not specific to one instance. Its meant to be called on the class itself
        return cls.number_of_animals
    
    @classmethod
    def add_animal(cls):
        cls.number_of_animals+=1

a1 = Animal("Victor")
a2 = Animal("Lilly")
print(Animal.number_of_animal())

# Example of static method
# Static method work as normal methods and are more of an organizational thing

class Math:
     
    @staticmethod
    def add5(x):
        return x+5
    
    @staticmethod
    def add10(x):
        return x+10
    
    @staticmethod
    def pr():
        print("run")
    
print(Math.add10(3))
    