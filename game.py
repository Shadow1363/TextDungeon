import os, random

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

HP = 50
HPMAX = HP
ATK = 3
pot = 1 # 30 HP
elix = 0 # 50 HP
gold = 0
x = 0
y = 0

map =[["plains", "plains", "plains", "plains", "forest", "mountain", "cave"],
      ["forest", "forest", "forest", "forest", "forest", "hills", "mountain"],
      ["forest", "fields", "bridge", "plains", "hills", "forest", "hills"],
      ["plains", "shop", "town", "mayor", "plains", "hills", "mountain"],
      ["plains", "fields", "fields", "plains", "hills", "mountain", "mountain"]]

biom = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "PLAINS",
        "e": False},
    "town": {
        "t": "TOWN CENTER",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "bridge": {
        "t": "BRIDGE",
        "e": False},
    "mayor": {
        "t": "MAYOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": False},
}

y_len = len(map)-1
x_len = len(map[0])-1

e_list = [
    "Goblin", "Orc", "Slime"
]

mobs = {
    "Goblin": {
        "hp": 15,
        "at": 3,
        "go": 8
    },
    "Orc": {
        "hp": 35,
        "at": 5,
        "go": 18
    },
    "Slime": {
        "hp": 30,
        "at": 2,
        "go": 12
    },
    "Dragon": {
        "hp": 100,
        "at": 8,
        "go": 100
    },
}

def shop():
    global buy, gold, pot, elix, ATK, HP
    
    while buy:
        clear()
        draw()
        print("Welcome to the shop!")
        draw()
        print("HP: " + str(HP) + "/" + str(HPMAX))
        print("ATK: " + str(ATK))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        print("GOLD: " + str(gold))
        draw()
        print("1 - BUY POTION (30HP) - 5 GOLD")
        print("2 - BUY ELIXIR (50HP) - 8 GOLD")
        print("3 - UPGRADE WEAPON (+2ATK) - 10 GOLD")
        print("4 - Leave")
        draw()
        
        choice = input("# ")
        
        if choice == "1":
            if gold >= 5:
                pot += 1
                gold -=5
                print("You bought a potion!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if gold >= 8:
                elix += 1
                gold -=8
                print("You bought a elixir!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "3":
            if gold >= 10:
                ATK += 2
                gold -=10
                print("You improved your weapon!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            buy = False
            
def cave():
    global boss, key, fight
        
    while boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do?")
        draw()
        print("1 - TURN BACK")
        if key == True:
            print("2 - USE KEY")
        draw()
        
        choice = input("# ")
        
        if choice == "1":
            boss = False
        elif choice =="2":
            if key == True:
                fight = True
                battle()

def mayor():
    global speak, key
    
    while speak:
        clear()
        draw()
        print("Hello there, " + name + "!")
        if ATK < 10:
            print("You're not strong enough to face the dragon yet!")
            key = False
        else:
            print("Now you might be strong enough, here take this key and good luck!")
            key = True
        draw()
        print("1 - LEAVE")
        draw()
        
        choice = input("# ")
        
        if choice == "1":
            speak = False
        
        

def heal(amount):
    
    global HP
    if HP + amount < HPMAX:
        HP+= amount
    else:
        HP = HPMAX

def clear():
    os.system("cls")

def draw():
    print("xX----------------------------Xx")

def save():
    lst = [ name, str(HP), str(ATK), str(pot), str(elix), str(gold), str(x), str(y), str(key)]
    with open("load.txt", 'w') as f:
        for item in lst:
            f.write(f'{item}\n')

def load() -> list:
    lst = []
    with open("load.txt", 'r') as f:
        for line in f:
            lst.append(line[0:-1])
    return lst

def battle():
    global fight, play, run, HP, pot, elix, gold, boss
    
    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]
    
    while fight:
        clear()
        draw()
        print("You encountered a " + enemy  + "!")
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(name + "'s HP: " + str(HP) + "/" + str(HPMAX))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP)")
        if elix > 0:
            print("3 - USE ELIXIR (50HP)")
        draw()
        
        choice = input("# ")
        
        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to  " + name + ".")
            input("> ")
        elif choice == "2":
           if pot > 0:
               pot -= 1
               heal(30)
               HP -= atk
               print(enemy + " dealt " + str(atk) + " damage to  " + name + ".")
               input("> ")
           else:
               print("No potions!")
               
        elif choice == "3":
            if elix > 0:
               elix -= 1
               heal(50)
               HP -= atk
               print(enemy + " dealt " + str(atk) + " damage to  " + name + ".")
               input("> ")
            else:
               print("No Elixirs!")
        
        if HP <= 0:
            clear()
            print(enemy + " defeated " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")
        if hp <= 0:
            clear()
            print(name + " defeated the " + enemy + "...")
            draw()
            input("> ")
            fight = False
            gold += g
            print("You've found " + str(g) + " gold!")
            if random.randint(0,100) < 30:
                pot += 1
                print("You've found a potion!")
            if enemy == "Dragon":
                draw()
                print("Congrats, you beat the game!")
                boss = False
                play = False
                run = False
            input("> ")

while run:
    while menu:
        clear()
        draw()
        print("1 - NEW GAME")
        print("2 - LOAD GAME")
        print("3 - RULES")
        print("4 - QUIT GAME")
        draw()
        
        if rules:
            print("Rules:")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")
        
        if choice == "1":
            name = input("What is your name, hero? ")
            menu = False
            play = True
        elif choice == "2":
            try:
                loaded_data = load()
                if len(loaded_data) != 9:
                    print("Error: The loaded file is corrupted.")
                    input("> ")
                else:
                    name, HP, ATK, pot, elix, gold, x, y, key = loaded_data
                    HP = int(HP)
                    ATK = int(ATK)
                    pot = int(pot)
                    elix = int(elix)
                    gold = int(gold)
                    x = int(x)
                    y = int(y)
                    if key == "True":
                        key == True
                    print("Welcome back, " + name + "!")
                    input("> ")
                    menu = False
                    play = True
            except OSError:
                print("No loadable file found")
                input("> ")
            
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()
            
    while play:
        save() # autosave
        clear()
        
        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()
                
        if play:
            draw()
            print("LOCATION: " + biom[map[y][x]]["t"])
            draw()
            
            print("NAME: " + name)
            print("HP: " + str(HP) + "/" + str(HPMAX))
            print("ATK: " + str(ATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("GOLD: " + str(gold))
            print("CORDS:", x, y)

            draw()
            print("0 - SAVE AND QUIT")
            if y > 0:
                print("1 - NORTH")
            if x < x_len:
                print("2 - EAST")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            if pot > 0:
                print("5 - USE POTION (30HP)")
            if elix > 0:
                print("6 - USE ELIXIR (50HP)")
            if map[y][x] == "shop" or map[y][x] == "mayor" or map[y][x] == "cave":
                print("7 - ENTER")
            
            draw()
            
            dest = input("# ")
            
            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                if pot > 0:
                    pot -=1
                    heal(30)
                else:
                    print("No potions!")
                input("> ")
                standing = True
            elif dest == "6":
                if elix > 0:
                    elix -=1
                    heal(50)
                else:
                    print("No Elixirs!")
                input("> ")
                standing = True
            elif dest == "7":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "mayor":
                    speak = True
                    mayor()
                if map[y][x] == "cave":
                    boss = True
                    cave()
            else:
                standing = True