# v2.0.0
# Tomás Martinez
# Dungeon Game

import time
import random
import os

def exploreDungeon(n,e):
 numPrints = random.randint(n, e)
 for _ in range(numPrints):
  time.sleep(timing)
  print("*")

def valueCalculator():
  for treasure in inventory:
    if treasure in possibleTreasures:
      if "Mysterious Orb" in inventory and "Dusty Book" in inventory:
       if treasure == "Mysterious Orb" or treasure == "Dusty Book":
        localValue = max(possibleTreasures[treasure])

      else:
       localValue = random.choice(possibleTreasures[treasure])
      
      value.append(localValue) 

inventory=[]
inventorySpace=1
inventoryPrice=300
timing=2
timingPrice=100
value=[]
money=0
finished=False
userInput=""

possibleTreasures = {
    "Golden Ring": [200, 100],
    "Silver Chalice": [70, 60, 110, 80],
    "Broken Sword": [12, 23, 60, 45],
    #"Crystal Crown": [350, 500, 50, 50,],
    #"Pearl Earings": [650, 100, 100, 100,],
    "Sack of Gold": [150],
    "Shattered Shield": [23, 25, 37, 55],
    "Dusty Book": [81, 20, 120, 200],
    "Mysterious Orb": [54, 99, 119, 250],
}

os.system('cls')

while not finished:
 print("Within the depths of the foreboding dungeon, you, an intrepid adventurer, set forth on a quest to collect treasures concealed in its mysterious depths.")
 time.sleep(timing)
 print("The echoes of forgotten whispers guide your every step as you navigate the treacherous labyrinth in pursuit of untold riches.")

 # Repeat until you have three treasures collected
 while len(inventory) < inventorySpace:
 
  # Make the user randomly wait between 2 to 6 timing.
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

  time.sleep(timing)
  print("You continue your descend.")

 exploreDungeon(2,6)

 # Print out the collected treausres
 print("Through the impenetrable darkness of the dungeon, a solitary light emerges, casting long, eerie shadows that dance upon ancient walls.")
 time.sleep(timing)
 print("To your astonishment, you have managed to escape the clutches of the dungeon, only to find yourself unexpectedly at the top, emerging triumphant into the realm of daylight.")
 time.sleep(timing)
 print("Behold, the treasures you have acquired in your daring escapade:")
 time.sleep(timing)

 plainInventory = inventory

 print(plainInventory)
 time.sleep(timing)

 valueCalculator()
 value = str(sum(value))

 if "Mysterious Orb" in inventory and "Dusty Book" in inventory:
  print("The dusty book you held in your hands, seemingly insignificant and neglected, now reveals itself as the key to unraveling the Orb's hidden knowledge.")
  print("You will sell them both for their highest value!")
 
 if "Shattered Shield" in inventory and "Broken Sword" in inventory:
  print("Just as you are on the verge of parting with them, the sword and shield astonishingly glow a bright blue, reverting to their original form.")
  print("The value of all your relics is instantly doubled!")
  value *= 2

 time.sleep(timing)
 print("You exchanged these precious relics, reaping the rewards they hold, for the following sum:")
 print("$" + value + ".")
 money +=int(value)
 value =[]
 print("You now have $" + str(money) + ".")
 time.sleep(timing)
 print("Pay $" + str(inventoryPrice) + " to get an extra inventory slot or you can pay $" + str(timingPrice) + " and go faster through dungeons.")
 userInput = str(input("To buy, type (inv/spd), for each respectively. Otherwise type (esc) to leave. "))

 if userInput.lower() == "inv" and int(money) >= int(inventoryPrice):
  print("You can now carry one extra treasure!")
  money-=inventoryPrice
  inventoryPrice*=2
  inventorySpace+=1
  inventoryPrice = int(inventoryPrice)

 elif userInput.lower() == "spd" and int(money) >= int(timingPrice):
  print("You now go through dungeons slightly faster!")
  money-=timingPrice
  timingPrice*=1.5
  timingPrice-=0.1

 elif userInput.lower() == "inv" and userInput.lower() == "spd":
  print("Seems like you don't have enough cash.")
 
 time.sleep(timing)
 print("Until next time!")
 print("")
 time.sleep(1)
 os.system('cls')
 inventory=[]