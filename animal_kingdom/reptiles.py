from animal_kingdom.basic_animal import Base
class Reptiles(Base):
    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.scaley_skin = True
        self.leathery_eggs = True
    def regain_energy(self, time):
        print('The reptile lays down in the sun to recharge their energy for', time, 'minutes')
    def stalk_prey(self):
        print('The reptile watches its prey from afar, waiting for the right moment to pounce')

crocodile = Reptiles()
crocodile.regain_energy(input('How long shall i rest for?'))
crocodile.stalk_prey()
crocodile.eating()
crocodile.sleeping()