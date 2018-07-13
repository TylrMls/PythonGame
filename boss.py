import random

def getBoss():
    return Boss()

class Boss:
    def __init__(self):
        self.health = random.randint(30, 40)
        self.damage = random.randint(1, 5)

    def isAlive(self):
        return self.health > 0
