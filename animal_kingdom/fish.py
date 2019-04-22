from animal_kingdom.basic_animal import Base
class Fish(Base):
    def __init__(self):
        super().__init__()
        self.gills = True
        self.fins = True
    def swimming(self):
        print('The Fish carefully swims in and out of the sea bed')
    def lateral_lines(self):
        print('Using the fishes lateral lines it detects water currents and even electricity')
shark = Fish()
shark.swimming()
shark.lateral_lines()
shark.eating()
shark.sleeping()