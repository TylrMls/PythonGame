import item as items
import random

class Player(object):
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 20

    def isAlive(self):
        return self.health > 0

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, name):
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            if item.name == name:
                self.inventory.pop(i)
                return

    def use(self, name):
        if self.hasItem(name):
            for item in items.items:
                if item.name == name:
                    self.health += item.healing

    def hasItem(self, name):
        for item in self.inventory:
            if item.name == name:
                return True
        return False

    def getItems(self):
        items = []
        for item in self.inventory:
            items.append(item.name)
        return items

    def useWeapon(self, name):
        for item in items.items:
            if item.name == name:
                item.uses += 1
                return item.damage

    def getUses(self, item):
        for i in items.items:
            if i.name == item:
                return i.uses

    def destroyItem(self):
        itemToRemove = random.choice(self.inventory)
        print("The enemy hit you and destroyed your {}!".format(itemToRemove.name))
        if itemToRemove.name == "Flower Pot":
            newItem = random.choice(items.items)
            self.inventory.append(newItem)
            print("You found {} in the Flower Pot!".format(newItem.name))
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            if item.name == itemToRemove.name:
                self.inventory.pop(i)
                return
