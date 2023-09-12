# 12/9/2023
# Tomás Martinez
# Dungeon Game

import time
import random

def exploreDungeon(n,e):
 numPrints = random.randint(n, e)
 for _ in range(numPrints):
  time.sleep(1)
  print("*")

inventory=[]
value=[]

possibleTreasures = {
    "Golden Ring": [200, 100],
    "Silver Chalice": [70, 60, 110, 80],
    "Broken Sword": [12, 23, 60, 43],
    "Crystal Crown": [300, 500, 50, 50,],
    "Pearl Earings": [650, 100, 100, 100,],
    "Sack of Gold": [150],
    "Shattered Shield": [23, 25, 37, 200],
    "Dusty Book": [81, 20, 120, 150],
    "Mysterious Orb": [54, 99, 119, 300]
}

print("Within the depths of the foreboding dungeon, you, an intrepid adventurer, set forth on a quest to collect treasures concealed in its mysterious depths.")
time.sleep(1)
print("The echoes of forgotten whispers guide your every step as you navigate the treacherous labyrinth in pursuit of untold riches.")

# Repeat until you have three treasures collected
while len(inventory) < 3:
 
 # Make the user randomly wait between 2 to 6 seconds.
 exploreDungeon(2,6)

 # Select a random treasure from all possibilities
 currentTreasure = random.choice(list(possibleTreasures.keys()))
 print("You came across a " + currentTreasure + ".")
 addItem = str(input("Do you pick it up? (Y/N) "))

 # If user types "Y" then add it to inventory.
 if addItem == "Y" or addItem == "y":
    inventory.append(currentTreasure)
    print("You have collected a " + currentTreasure + ".")
 else:
    print("You do not pick up the treasure.")

 time.sleep(1)
 print("You continue your descend.")

exploreDungeon(2,6)

# Print out the collected treausres
print("Through the impenetrable darkness of the dungeon, a solitary light emerges, casting long, eerie shadows that dance upon ancient walls.")
time.sleep(1)
print("To your astonishment, you have managed to escape the clutches of the dungeon, only to find yourself unexpectedly at the top, emerging triumphant into the realm of daylight.")
time.sleep(1)
print("Behold, the treasures you have acquired in your daring escapade:")
time.sleep(1)

for treasure in inventory:
    if treasure in possibleTreasures:
        localValue = random.choice(possibleTreasures[treasure])
        value.append(localValue)

inventory = ", ".join(inventory[:-1]) + " and " + inventory[-1] + "."

print(inventory)
time.sleep(1)
print("You have exchanged these precious relics, reaping the rewards they hold, for the following sum:")
time.sleep(1)
print("$" + str(sum(value)) + ".")