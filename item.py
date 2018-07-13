import random

# Confirm commit

class Item:
    def __init__(self, name, type, damage, healing, uses):
        self.name = name
        self.damage = damage
        self.healing = healing
        self.uses = uses
        self.type = type

specialItems = [
    Item("Gate Key", "Special", 0, 0, 0)
]

perGameItems = [
    Item("Teleporter", "Utility", 0, 0, 0)
]

items = [
    Item("Children's Advil", "Healing", 0, 10, 0),
    Item("Foam Sword", "Weapon", 2, 0, 0),
    Item("Stick", "Weapon", 5, 0, 0),
    Item("Sword", "Weapon", 10, 0, 0),
    Item("Water Bottle", "Healing/Weapon", 1, 5, 0),
    Item("Map", "Info", 0, 0, 0),
    Item("Key Map", "Info", 0, 0, 0),
    Item("Gate Map", "Info", 0, 0, 0),
    Item("Flower Pot", "Extra", 0, 0, 0)
]

def getRandomItem():
    return random.choice(items)

def doesExist(item):
    for i in items:
        if i.name == item:
            return True
    return False

def doesSpecialExist(item):
    for i in specialItems:
        if i.name == item:
            return True
    return False

def doesPerGameExist(item):
    for i in perGameItems:
        if i.name == item:
            return True
    return False

def addItem(item):
    for i in items:
        if i.name == item:
            return i
    for i in specialItems:
        if i.name == item:
            return i
    for i in perGameItems:
        if i.name == item:
            return i

def getSpecialItem(item):
    for i in specialItems:
        if i.name == item:
            return i

def getPerGameItem(item):
    for i in perGameItems:
        if i.name == item:
            return i

def isSpecialItem(item):
    for i in specialItems:
        if i.name == item:
            return True
    return False

def getType(item):
    for i in items:
        if i.name == item:
            return i.type
    for i in specialItems:
        if i.name == item:
            return i.type
    for i in perGameItems:
        if i.name == item:
            return i.type

def getName(item):
    for i in items:
        if i.name == item:
            return i.name
    for i in specialItems:
        if i.name == item:
            return i.name
    for i in perGameItems:
        if i.name == item:
            return i.name
