from animal_kingdom.basic_animal import Base
class Invertebrates(Base):
    def __init__(self):
        super().__init__()
        self.skeleton = False
        self.internal_skeleton = True
        self.backbone = True
    def metamorphosis(self):
        print('The invertebrate grows rapidly from a juvenile to a adult through metamorphsis')

worm = Invertebrates()
worm.metamorphosis()
worm.reproducing()
worm.sleeping()
worm.eating()
