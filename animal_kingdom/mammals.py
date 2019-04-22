from animal_kingdom.basic_animal import Base
class Mammals(Base):
    def __init__(self):
        super().__init__()
        self.hair = True
        self.fur = True
        self.warm_blooded = True
    def hunt(self):
        print('The mammal uses its vast senses and adaptability to hunt its prey no matter the enviroment')
    def pack(self):
        print('The pack leads ahead keeping safety in numbers')
    def milk_feed(self):
        print('The mammal lays down to feed its young with its milk')

wolf = Mammals()
wolf.hunt()
wolf.pack()
wolf.milk_feed()
wolf.sleeping()
