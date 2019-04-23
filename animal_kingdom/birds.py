from animal_kingdom.basic_animal import Base
class Birds(Base):
    def __init__(self):
        super().__init__()
        # Example of encapsulation 1
        self.feathers = True
        self.beaks = True
        self.warm_blooded = True
    def __adapt(self):
        print('The bird adapts to its surroundings')
    def fly(self):
        print('The bird flaps its wings and takes off with a great gust of air behind it')
    def nest(self):
        print('The bird makes a nest and sits on its eggs to provide them warmth')
        # Example of encapsulation 2
        self.__adapt()

owl = Birds()
owl.fly()
owl.nest()
owl.reproducing()
