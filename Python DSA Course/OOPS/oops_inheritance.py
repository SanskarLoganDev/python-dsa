class Pet:
    def __init__(self, name, age):
        self.name =  name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
    def speak(self):
        print("Hola Nino!")
        
class Cat(Pet):
    
    def __init__(self, name, age, color= "red"): # color = "red" defines the default value of color attribute if nothing is passed while function calling c.show()
        super().__init__(name, age) # reference the super/parent class, __init__ is the method that we want to call from the parent class
        # name and age are the arguments that we need to pass. We don't simply copy paste the attributes with self in child class as the parent class might be calling an important feature
        self.color = color
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. I am of {self.color} color")
    
    def speak(self):
        print("Meow")
        
class Dog(Pet):
    def speak(self):
        print("Bhow")
        
p = Pet("Victor", 12)
p.show()
p.speak()
c = Cat("Pity", 11)
c.show()
c.speak() # child class will overwrite the parent class if both have the same function
d = Dog("Doom", 10)
d.show()
d.speak()