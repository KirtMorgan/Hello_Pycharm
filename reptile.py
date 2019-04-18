from object_orientated_programming import Animal
# Inheritance practice, pass in the animal class to the reptile class
class Reptile(Animal):
    def __init__(self):
        super().__init__() # This line of code needs to be here to init as an animal as well
        self.cold_blooded = True
        self.heart_chambers =[3,4]

    def seek_heat(self):
        print('Need to find some sun')
    def hunt(self):
        print('Time to Hunt!')

# lizard = Reptile()
# lizard.seek_heat()

