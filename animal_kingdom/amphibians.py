from animal_kingdom.basic_animal import Base
class Amphibians(Base):
    def __init__(self):
        super().__init__()
        self.wet_skin = True
        self.lives_near_water = True
    def maintain_moisture(self):
        print('To maintain moisture the amphibian jumps into a body of water')
    def lay_eggs(self):
        print('The amphibian jumps over to the body of water to begin laying its eggs')

frog = Amphibians()
frog.lay_eggs()
frog.maintain_moisture()
frog.reproducing()
frog.eating()