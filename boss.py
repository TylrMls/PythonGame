import random

def getBoss():
    return Boss()

class Boss:
    def __init__(self):
        self.health = random.randint(30, 40)
        self.damage = random.randint(10, 20)

    def isAlive(self):
        return self.health > 0
