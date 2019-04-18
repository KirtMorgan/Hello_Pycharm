# Object orientated programing
# The context of objects and defining what they are into code
# 4 pillars: obstraction, polymorphism, Encapsulation, inheritance

#creating a class
class Animal:
# Define how it looks (in terms of code)
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True
# Create methods for this class object
    def breathe(self):
        print("Breathing good")

    def eat(self):
        print('NOM')

    def potty(self):
        print('Going down to brown town')

# dog = Animal()
# dog.breathe()
# dog.eat()
# dog.potty()