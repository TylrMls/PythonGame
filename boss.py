import random

def getBoss():
    return Boss()

class Boss:
    def __init__(self):
        self.health = random.randint(15, 30)
        self.damage = random.randint(5, 15)

    def isAlive(self):
        return self.health > 0
