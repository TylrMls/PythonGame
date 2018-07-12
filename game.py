import location, player, random, enemy, time, os, boss
import item as items
from datetime import datetime

seed = input("Enter a seed: ")

tile = location.Location(seed + "0,0")

user = player.Player(input("What is your name: "))

keyFindx = random.randint(-25, 25)
keyFindy = random.randint(-25, 25)

gateFindx = random.randint(-25, 25)
gateFindy = random.randint(-25, 25)

gateMapx = random.randint(gateFindx - 1, gateFindx + 1)
gateMapy = random.randint(gateFindy - 1, gateFindy + 1)

keyMapx = random.randint(keyFindx - 1, keyFindx + 1)
keyMapy = random.randint(keyFindy - 1, keyFindy + 1)

key = "{},{}".format(gateFindx, gateFindy)

x = 0
y = 0
tiles = {}
searched_tiles = []

# print("{}, {}".format(gateFindx, gateFindy))
# For debug perposes

def move(direction):
    global x, y
    if direction == "n":
        y += 1
    elif direction == "e":
        x += 1
    elif direction == "s":
        y -= 1
    elif direction == "w":
        x -= 1

    key = "{},{}".format(x, y)
    if key in tiles:
        return tiles[key]
    else:
        newtile = location.Location(seed + key)
        if x == gateFindx and y == gateFindy:
            newtile.name = "The Gate"
        tiles[key] = newtile
        return newtile

def debugMode(tile):
    global x, y, debugOn
    print("You have entered debug mode!")
    debugOn = True
    while debugOn:
        print("Location: {}, on grid location {}, {}".format(tile.name, x, y))
        cmd = input("$ > ")
        if cmd.lower() == "changex":
            amountChange = input("New x: ")
            x = int(amountChange)
            tile = move("debug")
        elif cmd.lower() == "changey":
            amountChange = input("New y: ")
            y = int(amountChange)
            tile = move("debug")
        elif cmd.lower() == "exit":
            debugOn = False
        elif cmd.lower().startswith("additem"):
            _, item1 = cmd.split(" ", 1)
            if items.doesExist(item1):
                user.addItem(items.addItem(item1))
                print("Added item: {}".format(item1))
            else:
                print("That item does not exist!")
        elif cmd.lower().startswith("addspecialitem"):
            _, item2 = cmd.split(" ", 1)
            if items.doesSpecialExist(item2):
                user.addSpecialItem(items.getSpecialItem(item2))
                print("Added item: {}".format(item2))
            else:
                print("That item does not exist!")
        elif cmd.lower() == "keylocation":
            print("Key Location: {}, {}".format(keyFindx, keyFindy))
        elif cmd.lower() == "gatelocation":
            print("Gate Location: {}, {}".format(gateFindx, gateFindy))
        elif cmd.lower() == "sethealth":
            setHealth = input("New health: ")
            user.health = int(setHealth)
        else:
            print("That is not a command")

def bossBattle():
    commandRun = False
    os.system('cls')
    bossFight = boss.getBoss()
    print("As you open the gates, you see a heavily armoured enemy emerge from them...")
    time.sleep(3)
    while bossFight.isAlive() and user.isAlive():
        print("You have {} health! Enemy has {} health!".format(user.health, bossFight.health))
        command = input("FIGHT MODE > ")
        if command == "punch":
            commandRun = True
            if random.randint(1, 10) < 10:
                print("You punched the enemy!")
                bossFight.health -= 1
            else:
                print("You are clumsy and missed the punch!")
        elif command == "curb stomp":
            commandRun = True
            if random.randint(1, 5) == 1:
                print("Wow! a hit!")
                bossFight.health -= 5
            else:
                print("What a horrible attempt!")
        elif command == "items":
            if user.inventory:
                print("You have: {}".format(user.getItems()))
            else:
                print("You have no items")
        elif command.startswith("use"):
            if command == "use" or command == "use ":
                print("You must specify what item to use")
            else:
                _, item = command.split(" ", 1)
                if user.hasItem(item):
                    if items.getType(item) == "Weapon" or items.getType(item) == "Healing/Weapon":
                        commandRun = True
                        print("Used {}".format(item))
                        bossFight.health -= user.useWeapon(item)
                        if user.getUses(item) == 3:
                            user.removeItem(item)
                            print("Your {} broke".format(item))
                        if items.getType(item) == "Healing/Weapon":
                            user.removeItem(item)
                            print("You used your {} to attack".format(item))
                    else:
                        print("Can't use {} to fight".format(item))
                else:
                    print("You don't have a {}!".format(item))
        if bossFight.health > 0 and commandRun:
            user.health -= bossFight.damage
            if random.randint(1, 3) == 1:
                user.destroyItem()
            commandRun = False

running = True
while running and user.isAlive():
    if tile.name == "The Gate":
        print("You have come across a massive gate, leading to an unknown place")
    else:
        print("You are in {}".format(tile.name))
    if tile.enemy and tile.enemy.isAlive():
        print("There is an enemy here! They have {} health".format(tile.enemy.health))
    command = input("> ")
    if command.lower() == "items":
        if user.inventory:
            print("You have: {}".format(user.getItems()))
        else:
            print("You have no items")
    elif command.lower() == "move":
        if tile.enemy and tile.enemy.isAlive():
            print("You cannot move. There are enemies nearby")
        else:
            direction = input("N/E/S/W > ")
            if direction == "":
                print("You must give a direction")
            elif direction[0].lower() == "n":
                print("Go North")
                tile = move("n")
            elif direction[0].lower() == "e":
                print("Go East")
                tile = move("e")
            elif direction[0].lower() == "s":
                print("Go South")
                tile = move("s")
            elif direction[0].lower() == "w":
                print("Go West")
                tile = move("w")
            else:
                print("Moving Cancelled")
    elif command.lower() == "debug":
        debugMode(tile)
        tile = move("debug")
    elif command.lower() == "search":
        if tile.seed in searched_tiles:
            print("You have already searched here")
            continue
        random.seed(seed + str(x) + str(y))
        if x == keyFindx and y == keyFindy:
            print("You have discovered an old Gate Key!")
            user.addItem(items.addItem("Gate Key"))
        elif random.randint(1, 5) == 1:
            print("You seem to have found something")
            user.addItem(items.getRandomItem())
        else:
            print("You search for a while, but find nothing")
        searched_tiles.append(tile.seed)
    elif command.lower() == "fight":
        random.seed(datetime.now())
        while tile.enemy.isAlive() and user.isAlive():
            print("You have {} health! Enemy has {} health!".format(user.health, tile.enemy.health))
            commandRun = False
            command = input("FIGHT MODE > ")
            if command.lower() == "punch":
                if random.randint(1, 10) < 10:
                    print("You punched the enemy!")
                    tile.enemy.health -= 1
                    commandRun = True
                else:
                    print("You are clumsy and missed the punch!")
                    commandRun = True
            elif command.lower() == "curb stomp":
                if random.randint(1, 5) == 1:
                    print("Wow! a hit!")
                    tile.enemy.health -= 5
                    commandRun = True
                else:
                    print("What a horrible attempt!")
                    commandRun = True
            elif command.lower() == "items":
                if user.inventory:
                    print("You have: {}".format(user.getItems()))
                else:
                    print("You have no items")
            elif command.lower().startswith("use"):
                if command.lower() == "use" or command.lower() == "use ":
                    print("You must specify what item to use")
                else:
                    _, item = command.split(" ", 1)
                    if user.hasItem(item):
                        if items.getType(item) == "Weapon" or items.getType(item) == "Healing/Weapon":
                            print("Used {}".format(item))
                            tile.enemy.health -= user.useWeapon(item)
                            commandRun = True
                            if user.getUses(item) == 3:
                                user.removeItem(item)
                                print("Your {} broke".format(item))
                            if items.getType(item) == "Healing/Weapon":
                                user.removeItem(item)
                                print("You used your {} to attack".format(item))
                        else:
                            print("Can't use a {} to fight".format(item))
                    else:
                        print("You don't have a {}!".format(item))
            if tile.enemy.health > 0 and commandRun:
                user.health -= tile.enemy.damage
            elif tile.enemy.health <= 0:
                if random.randint(1, 5) == 1:
                    itemRecieved = items.getRandomItem()
                    user.addItem(itemRecieved)
                    print("You killed the enemy and they dropped a {}!".format(itemRecieved.name))
                else:
                    print("You killed the enemy!")
    elif command.lower().startswith("use"):
        if command.lower() == "use" or command.lower() == "use ":
            print("You must specify what item to use")
        else:
            _, item = command.split(" ", 1)
            if user.hasItem(item):
                if items.getType(item) == "Info":
                    if items.getName(item) == "Map":
                        print("You look at your map and determine you are around the coordinates {}, {}".format(x, y))
                    elif items.getName(item) == "Gate Map":
                        print("You look at the Gate Map and discover a red circle around the general area of {}, {}".format(gateMapx, gateMapy))
                    elif items.getName(item) == "Key Map":
                        print("You look at the Key Map and discover a red circle around the general area of {}, {}".format(keyMapx, keyMapy))
                elif items.isSpecialItem(item) and tile.name != "The Gate":
                    print("This is a special item! You cannot use it here")
                elif items.isSpecialItem(item) and tile.name == "The Gate":
                    bossBattle()
                elif items.getType(item) == "Weapon":
                    print("This is a fighting item. you cannot use that right now")
                else:
                    print("You have used {}".format(item))
                    user.use(item)
                    user.removeItem(item)
            else:
                print("You don't have {}".format(item))
    elif command == "":
        print("You must give a command")
