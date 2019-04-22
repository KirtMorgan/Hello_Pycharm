from animal_kingdom.basic_animal import Base
class Birds(Base):
    def __init__(self):
        super().__init__()
        # Example of encapsulation
        self._feathers = True
        self.beaks = True
        self.warm_blooded = True
    def adapt(self):
        print('The bird adapts to its surroundings')
    def fly(self):
        print('The bird flaps its wings and takes off with a gust of air behind it')
    def nest(self):
        print('The bird makes a nest and sits on its eggs to provide them warmth')

owl = Birds()
owl.adapt()
owl.fly()
owl.nest()
owl.reproducing()
