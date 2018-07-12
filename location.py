import random, enemy

descriptions = ["Hollow", "Quiet", "Whistling", "Mesmerizing", "Shrek's"]
location_types = ["Forest", "River", "Cave", "Fields", "Swamp", "Desert", "Mountain", "Valley", "Tundra"]

class Location:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
        self.name = "{} {}".format(
                random.choice(descriptions),
                random.choice(location_types)
            )
        self.enemy = enemy.get()
