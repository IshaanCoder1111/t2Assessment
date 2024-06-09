import os, time, random

inventory = {
     "bread": 0,
     "armour": 0,
     "meat": 0,
     "coin": 0,
     "vegetable": 0,
     "knife": 0,
     "jewellery": 0,
     "wine glass": 0,
     "medicine": 0,
     "oil": 0,
     "sword": 0,
     "land ownership": 0,
     "wine": 0,
     "key": 0
     }

#Adding a clear function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

#Loading Function
loading = ["Loading👑", "Loading.👑", "Loading..👑", "Loading...👑"]
def gameloading():
    for i in loading:
                print(i)
                time.sleep(0.5)
                clear()

#Starting Game
def startermenu():
    clear()
    print("Welcome To")
    print("""
        _       _________ _        _______    _______  _______   _________          _______    _______  _______  _______ _________ _        _______ 
        | \    /\\__   __/( (    /|(  ____ \  (  ___  )(  ____ \  \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ \\__   __/( \      (  ____ \
        |  \  / /   ) (   |  \  ( || (    \/  | (   ) || (    \/     ) (   | )   ( || (    \/  | (    \/| (   ) || (    \/   ) (   | (      | (    \/
        |  (_/ /    | |   |   \ | || |        | |   | || (__         | |   | (___) || (__      | |      | (___) || (_____    | |   | |      | (__    
        |   _ (     | |   | (\ \) || | ____   | |   | ||  __)        | |   |  ___  ||  __)     | |      |  ___  |(_____  )   | |   | |      |  __)   
        |  ( \ \    | |   | | \   || | \_  )  | |   | || (           | |   | (   ) || (        | |      | (   ) |      ) |   | |   | |      | (      
        |  /  \ \___) (___| )  \  || (___) |  | (___) || )           | |   | )   ( || (____/\  | (____/\| )   ( |/\____) |   | |   | (____/\| (____/\
        |_/    \/\_______/|/    )_)(_______)  (_______)|/            )_(   |/     \|(_______/  (_______/|/     \|\_______)   )_(   (_______/(_______/
                                                                                                                                                               
          """)
    input("Press Enter To Continue!: ")
    clear()

def nameselection():
    clear()
    print("Choose a Fierce Name to Proceed!")
    while True:
        global namechosen
        namechosen = input("Chosen Name(No More Than 10 Characters): ") 
        if 0 < len(namechosen) <= 10:
            print(f"WELCOME TO KING OF THE CASTLE {namechosen.upper()}")
            input("Press any enter to continue: ")
            gameloading()
            break
        elif len(namechosen) >= 10:
            print("That name is too long!")
            time.sleep(1.5)  
        else:
            print("Type a letter at least!")
            time.sleep(1.5)
    clear()

def endgame():
          clear()
          if character.is_alive == True:
               print("Finished Game")
          if character.is_alive == False:
               print("You Lost")
          input("Press Any Key To Continue")
          exit()

def inventory_function(item_received):
    print("Item received")
    inventory[item_received.lower()] += 1
    if item_received == "coin":
        character.money += items_dictionary["coin"].value
        inventory["coin"] -= 1
    print("Your inventory consists of:")
    for item, quantity in inventory.items():
        print(f"{item.upper()}: {quantity}")  

class Cell:
    def __init__(self):
        self.area = None

class Area:
    def __init__(self,name,description,coordinates,areaitems,areaenemies):
        self.name = name
        self.description = description
        self.coordinates = coordinates
        self.areaitems = areaitems
        self.areaenemies = areaenemies

    def insidearea(self, x, y):
        return (x, y) in self.coordinates

class WorldMap:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.grid = [[Cell() for i in range(width)]for i in range(height)]

    def add_area(self, area):
        for x, y in area.coordinates:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y][x].area = area

    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

world_map = WorldMap(20,19)

Hut_village = Area("Hut","Your home.",[(1,1)],["Knife"],["Nothing"])
Village = Area("Village","The home of the villagers.",[(1,2),(1,3),(1,4),(1,5),(1,6),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6)],["bread","coin","vegetable"],["animal","citizen"]) 
Ocean = Area("Ocean","Enter with the risk of death.",[(x, 0) for x in range(20)] + [(x, 18) for x in range(20)] + [(0, y) for y in range(1, 19)] + [(19, y) for y in range(1, 19)],["Nothing"],["Nothing"])
Castle = Area("Castle","King's home.",[(8,10),(8,11),(8,12),(8,13),(9,10),(9,11),(9,12),(9,13),(10,10),(10,11),(10,12),(10,13),(11,10),(11,11),(11,12),(11,13)],["Crown","Royal_Mantle"],["King"]) 
Merchant_farm = Area("Merchant_farm","The farm of resources.",[(11,2),(12,2),(13,2),(14,2),(15,2),(16,2),(17,2),(18,2),(11,3),(12,3),(13,3),(14,3),(15,3),(16,3),(17,3),(18,3),(11,4),(12,4),(13,4),(14,4),(15,4),(16,4),(17,4),(18,4),(11,1),(12,1),(13,1),(14,1),(15,1),(16,1),(17,1),(18,1)],["Jewellery","Wine_glass","Oil","Medicine","Wine"],["Merchant"]) 
Forest = Area("Forest","Enter at your own risk.",[(2,15),(2,16),(2,17),(3,15),(3,16),(3,17),(4,15),(4,16),(4,17),(1,15),(1,16),(1,17)],["Nothing"],["Animal"]) 
Estate = Area("Estate","Home of the nobles.",[(16,13),(16,14),(16,15),(16,16),(16,17),(17,13),(17,14),(17,15),(17,16),(17,17),(18,13),(18,14),(18,15),(18,16),(18,17)],["Key","Land"],["Noble","Knights"]) 


world_map.add_area(Hut_village)
world_map.add_area(Village)
world_map.add_area(Ocean)
world_map.add_area(Castle)
world_map.add_area(Merchant_farm)
world_map.add_area(Forest)
world_map.add_area(Estate)


barren_land_coordinates = [(x, y) for y in range(world_map.height) for x in range(world_map.width) if world_map.get_cell(x, y).area is None]
Barren_Land = Area("Barren Land", "Uninhabited Land.", barren_land_coordinates, ["Nothing"], ["Nothing"])

world_map.add_area(Barren_Land)

"""def print_world_map(world_map, character):
    for y in range(world_map.height):
        for x in range(world_map.width):
            cell = world_map.get_cell(x, y)
            if character.x == x and character.y == y:
                 print("P", end=" ")
            elif cell and cell.area:
                print(cell.area.name[0], end=' ')
            else:
                print('.', end=' ')
        print()"""

def print_world_map(world_map, character):
     import cv2
     img = cv2.imread("Map.png")
     cv2.imshow('map', img)
     cv2.waitKey(0) 
     cv2.destroyAllWindows()


def attackingfunction(enemy):
     while True:
          print(f"You have encountered {enemy}")
          fightorflight = input("Do you choose to flee or fight\nNote: Fleeing results in a 5 healthpoint deduction\nChoice: ").strip().lower()
          if "fight" in fightorflight:
               character.attacking(enemy_var=enemy)
          if "flee" in fightorflight:
               character.health -= 5
               print(f"You are currently on {character.health} from {enemy} hitting you from behind")
               movingcharacter()
          else:
               print("Thats not an option")
               time.sleep(2)

class Entity:
     def __init__(self, health, is_alive, power):
          self.health = health
          self.is_alive = is_alive
          self.power = power                 
         

class Character(Entity):
     def __init__(self, health, is_alive, power, stamina, hunger, money, max_health, x_start, y_start, world_map):
          super().__init__(health, is_alive, power)
          self.stamina = stamina
          self.hunger = hunger
          self.money = money
          self.max_health = max_health
          self.x = x_start
          self.y = y_start
          self.world_map = world_map
          self.visited_noble = False
          self.visited_knight = False

     def consuming(self, item):
          self.health += item.health
          self.power += item.power
          self.hunger += item.hunger
          self.stamina += item.stamina
          if item.name in ["vegetable","meat", "bread", "medicine"]:
               print(f"The {item} has been removed from your inventory")
               inventory.remove(item.name)
               if self.health > self.max_health:
                    self.health = self.max_health
          else:
               print("What a silly try, you cannot consume this item")
               self.health -= item.health 
               self.power -= item.power
               self.hunger -= item.hunger
               self.stamina -= item.stamina

     
     def movement(self, direction):
        self.stamina -= 3
        self.hunger += 3
        directions = {
            "north": (0, -1),
            "south": (0, 1),
            "east": (1, 0),
            "west": (-1, 0) 
        }
        if direction in directions:
          move_x, move_y = directions[direction]
          x_change, y_change = self.x + move_x, self.y + move_y
          if 0 <= x_change < self.world_map.width and 0 <= y_change < self.world_map.height:
               self.x, self.y = x_change, y_change
               print(f"Moved to coordinates: ({self.x}, {self.y})") 
               if (self.x, self.y) == (11, 3):
                    clear()
                    print(f"{namechosen}: HUH... whe..where am I?")
                    time.sleep(2)
                    print("""Merchant: Welcome young one! You have finally found me. I've heard plenty about you and am well aware of your intentions.
By coming here you will be able to buy and sell items to continue your journey and fulfil your quest to takeover the throne.
You are able to come here anytime throughout your journey to earn a valuable. 
Now what would you like to do, if you buy an item I promise not to tell the king🤫""") 
                    input("Press enter to continue: ")
                    clear()
                    merchant()
               if (self.x, self.y) == (17,15) and self.visited_noble == False:
                    self.visited_noble = True
                    clear()
                    time.sleep(1)
                    print("""NOBLE: Ha! You really think you can get the key from me! How silly of you. 
       You'll never avenge your mother. I was able to take her life 20 years ago. 
       Now I'll take yours.""")
                    input("Press Enter to Continue")
                    clear()
                    attackingfunction("Noble")     
               if (self.x, self.y) in [(17,14), (16,15), (17,16), (18,15)] and self.visited_knight == False:
                    self.visited_knight = True
                    print("""KNIGHT: HEY! WHAT IS A PEASANT DOING IN THE ESTATE?!?! """)  
                    input("Press Enter to Continue: ")
                    attackingfunction("Knight")            
               if (self.x, self.y) == (9,10):
                    attackingfunction("King")
                    if "crown" or "royal mantle" in inventory:
                         clear()
                         print("KING: NOOOO! You have dethroned me!") 
                         time.sleep(3)
                         clear()
                         print("YOU WON 👑🤴")
                         runitback = input("Type and Enter 'm' to go back to main menu or 'q' to quit")
                         if runitback == "q":
                              exit
                         elif runitback == "m":
                              startermenu()
                              nameselection()
                              dametime()
                         else: 
                              print("Try again. You have entered an invalid input. ")
                         


               cell = self.world_map.get_cell(self.x, self.y)
               if cell and cell.area:
                    if cell.area.name == "Ocean":
                         print("You have entered the ocean and died")
                         time.sleep(2)
                         self.is_alive = False
                         endgame()
                    if cell.area.name == "Castle":
                         if "key" in inventory:
                              print("You have unlocked the gates and have enetered the castle")
                         else:
                              print("You need to get the key from the noble to unlock the gates to the castle.")
                              self.x, self.y = self.world_map.width // 2, self.world_map.height // 2
                    else:
                         print(f"You move {direction} to the {cell.area.name}.")
          else:
               print("You can't go that way.")
        else:             
          print("Invalid direction.")
               
     def attacking(self, enemy_var):
          self.stamina -= 3
          self.hunger += 3
          if isinstance(enemy_var, str):
            enemy_var = all_enemy_dict[enemy_var]
          hitormiss2 = random.randint(1,2)
          if hitormiss2 == 1:
            print(f"{namechosen} has missed their attack, oh no!")
            time.sleep(1.5)
            enemy_var.attacking(enemy_var=enemy_var)
          if hitormiss2 == 2:
               print(f"{namechosen} has hit the {enemy_var} for {self.power} damage")
               time.sleep(1.5)
               enemy_var.damage_taken(enemy_var=enemy_var)
      

     def damage_taken(self, damage, enemy_var):
          self.health -= damage
          self.status_check(enemy_var=enemy_var)

     def status_check(self, enemy_var):
          if self.health <= 0:
               print(f"{namechosen} has been vanquished, game over🥲")
               self.is_alive = False
               endgame()
          if self.health > 0:
               print(f"{namechosen} has {self.health} hearts left")
               time.sleep(1.5)
               self.attacking(enemy_var=enemy_var)



class Enemy(Entity):
     def __init__(self, health, is_alive, power, enemy_name, loot_options, type_move):
          super().__init__(health, is_alive, power)
          self.enemy_name = enemy_name
          self.loot_options = loot_options
          self.type_move = type_move
     
     def __str__(self):       
          return self.enemy_name

     def check_status(self, enemy_var):
          if self.health <= 0:
               print(f"{enemy_var} has been vanquished by {namechosen}, congrats soldier!")
               self.is_alive = False
               self.items_dropped()
          if self.health > 0:
               print(f"{enemy_var} has {self.health} hearts left")
               time.sleep(1.5)
               self.attacking(enemy_var)
                
     def attacking(self, enemy_var):
        hitormiss = random.randint(1,2)
        if hitormiss == 1:
            print(f"{enemy_var} has missed their attack, this is your chance {namechosen}!")
            time.sleep(1.5)
            character.attacking(enemy_var=enemy_var)
        if hitormiss == 2:
            enemy_move = random.choice(self.type_move)
            print(f"{enemy_var} has hit the {namechosen} with {enemy_move} for {self.power} damage, ow!")
            time.sleep(1.5)
            character.damage_taken(damage=self.power, enemy_var=enemy_var)
                       
     def damage_taken(self, enemy_var):
          self.health -= character.power
          self.check_status(enemy_var)

     def items_dropped(self):
          global loot
          loot = random.choice(self.loot_options)
          if loot == None:
               print("No item has been dropped")
               movingcharacter()    
          input(f"Congratulations You Have Acquired The {loot} Item, press enter to continue")      
          if loot == "meat":
               inventory_function("meat")
               movingcharacter()             
          if loot == "vegetable":
               inventory_function("vegetable")
               movingcharacter()              
          if loot == "bread":
               inventory_function("bread")
               movingcharacter()
          if loot == "coin":
               character.money += coin.value
               movingcharacter()
          if loot == "sword":
               print("Your knife is thrown away")
               inventory.remove("knife")
               character.power -= 20
               character.stamina -= 10
               inventory_function("sword")
               movingcharacter()
          if loot == "armour":
               character.max_health = 200
               inventory_function("armour")
               movingcharacter()
          
          



tiger = Enemy(health=random.randint(95, 105), is_alive=True, power=50, enemy_name="Tiger", loot_options=[None, "meat"], type_move=["Scratch", "Bite"])
bear = Enemy(health=random.randint(80,90), is_alive=True, power=40, enemy_name="bear", loot_options=[None, "meat"], type_move=["Scratch", "Tackle"])
stray_dog = Enemy(health=30, is_alive=True, power=10, enemy_name="Stray Dog", loot_options=["meat"], type_move=["Rabies", "Bite", "Scratch"])
citizen_names = ["Jack", "Fred", "Amelia"]
citizen = Enemy(health=50, is_alive=True, power=5, enemy_name= random.choice(citizen_names), loot_options=["bread", "vegetables", "coin", None], type_move=["Slap", "Punch", "Kick", "Choke"])
knight = Enemy(health=100, is_alive=True, power=20, enemy_name="Knight", loot_options=["armour", "sword", "helmet"], type_move=["Stab", "Slash"])
noble = Enemy(health=200, is_alive=True, power=40, enemy_name="Noble", loot_options=["land", "key"], type_move=["Money Shower", "Dollar Roller", "Cash Slam"])
king = Enemy(health=500, is_alive=True, power=60, enemy_name="King", loot_options=["crown", "royal mantle"], type_move=["Fireball", "Ice Spray"])

all_enemy_dict = {
    "Tiger": tiger,
    "Bear": bear,
    "Stray Dog": stray_dog,
    "Citizen": citizen,
    "Knight": knight,
    "Noble": noble,
    "King": king
}
    
     

class Item:
    def __init__(self, power, stamina, hunger, value, health, name):
        self.power = power
        self.stamina = stamina
        self.hunger = hunger 
        self.value = value
        self.health = health
        self.name = name

    def __str__(self):       
          return self.name
          
     

bread = Item(2, 2, -3, 0, 1, "bread")
armour = Item(10, 0, 0, 30, 100, "armour")
meat = Item(2, 2, -5, 0, 2, "meat")
coin = Item(0, 0, 0, 1, 0, "coin")
vegetable = Item(0, 5, -3, 0, 2, "vegetable")
knife = Item(20, 0, 0, 10, 0, "knife")
jewellery = Item(0, 0, 0, 5, 0, "jewellery")
wineglass = Item(0, 0, 0, 5, 0, "wineglass")
medicine = Item(0, 0, 0, 8, 20, "medicine")
oil = Item(0, 0, 0, 3, 0, "oil")
sword = Item(50, 5 , 0, 30, 0, "sword")
land = Item(0,0,0,50,0,"land ownership") 
wine = Item(1,-2,-1,5,-2,"wine")
key = Item(0,0,0,0,0,"key")

items_dictionary = {
    "bread": bread,
    "armour": armour,
    "meat": meat,
    "coin": coin,
    "vegetable": vegetable,
    "knife": knife,
    "jewellery": jewellery,
    "wine glass": wineglass,
    "medicine": medicine,
    "oil": oil,
    "sword": sword,
    "land ownership": land,
    "wine": wine,
    "key": key
}

def barren_enemy_detection(character, cell):
     enemychances = ["Stray Dog", "Citizen", None, None, None, None, None,]
     enemy_detection = random.choice(enemychances)
     if enemy_detection:
          attackingfunction(enemy_detection)
     else:
          print("There are no enemies in sight, keep moving soldier!")

def village_enemy_detection(character, cell):
     enemychances = ["Stray Dog", "Citizen"]
     enemy_detection = random.choice(enemychances)
     if enemy_detection:
          attackingfunction(enemy_detection)
     else:
          print("There are no enemies in sight, keep moving soldier!")


def forest_enemy_detection(character, cell):
     animal_selection = random.randint(1, 2)
     if animal_selection == 1:
          attackingfunction("Tiger")
     if animal_selection == 2:
          attackingfunction("Bear")
          
          
def collect_items_barren_land(character, cell):
    items_chances = ["coin", "vegetable", "bread", None]  
    collect_item = random.choice(items_chances)  
    if collect_item:
        print(f"You found some {collect_item.upper()} while roaming the land!")
        inventory_function(collect_item)
    else:
        print("There are no items here. Keep on searching!")

def collect_items_village(character, cell):
    items_chances = ["coin", "vegetable", "bread", None]  
    collect_item = random.choice(items_chances)  
    if collect_item:
        print(f"You found some {collect_item.upper()} while roaming the village!")
        inventory_function(collect_item)
    else:
        print("There are no items here. Keep on searching!")

def collect_items_merchant_farm(character, cell):
    items_chances = ["oil","medicine","wine glass","jewellery","wine", None]  
    collect_item = random.choice(items_chances)  
    if collect_item:
        print(f"You found some {collect_item.upper()} while roaming the farm!")
        inventory_function(collect_item)
    else:
        print("There are no items here. Keep on searching!")

def collect_items_estate(character, cell):
    items_chances = ["armour", "land", None]  
    collect_item = random.choice(items_chances)  
    if collect_item:
        print(f"You found some {collect_item.upper()} while roaming the estate!")
        inventory_function(collect_item)
    else:
        print("There are no items here. Keep on searching!")


def merchant():
    while True:
        clear()
        print("WELCOME TO THE MERCHANT!")
        character_choice = input("Would you like to 'buy', 'sell', or 'exit'? ").strip().lower()

        if character_choice == "sell":
            while True:
                clear()
                print("What would you like to sell?")
                print("Your inventory:")
                for item, quantity in inventory.items():
                    if quantity > 0:
                        print(f"{item.capitalize()}: {quantity}")
                item_to_sell = input("Enter the item name (or type 'back' to return): ").strip().lower()
                if item_to_sell == "back":
                    break
                elif item_to_sell in inventory and inventory[item_to_sell] > 0:
                    sell_price = items_dictionary[item_to_sell].value
                    print(f"Selling {item_to_sell} for {sell_price} coins.")
                    confirm = input("Confirm sale? (yes/no): ").strip().lower()
                    if confirm == "yes":
                        inventory[item_to_sell] -= 1
                        character.money += sell_price
                        print(f"You sold {item_to_sell} for {sell_price} coins.")
                    else:
                        print("Sale canceled.")
                else:
                    print("Item not in inventory or you don't have any.")
                time.sleep(1.5)

        elif character_choice == "buy":
            while True:
                clear()
                print("What would you like to buy?")
                for item, details in items_dictionary.items():
                    if item != "coin":
                        print(f"{item.capitalize()} - {details.value} coins")
                print(f"Your money: {character.money} coins")
                item_to_buy = input("Enter the item name (or type 'back' to return): ").strip().lower()
                if item_to_buy == "back":
                    break
                elif item_to_buy in items_dictionary:
                    buy_price = items_dictionary[item_to_buy].value
                    if character.money >= buy_price:
                        print(f"Buying {item_to_buy} for {buy_price} coins.")
                        confirm = input("Confirm purchase? (yes/no): ").strip().lower()
                        if confirm == "yes":
                            inventory_function(item_to_buy)
                            character.money -= buy_price
                            print(f"You bought {item_to_buy} for {buy_price} coins.")
                        else:
                            print("Purchase canceled.")
                    else:
                        print("Not enough coins.")
                else:
                    print("Item not available.")
                time.sleep(1.5)

        elif character_choice == "exit":
            break
        else:
            print("Invalid choice. Please type 'buy', 'sell', or 'exit'.")
            time.sleep(1.5)

def consuming_food():
          edible_items = []        
          for food in inventory:
               if food in ["vegetable", "bread", "medicine", "meat"]:
                    edible_items.append(food)
               else: 
                    pass
          print("The items that are edible within your inventory are" + ', '.join(edible_items))
          consumed_item = input("What item would you like to eat, or would you like to exit?: ").strip().lower()
          while True:
               if consumed_item in edible_items:
                    print(f"Eating the {consumed_item}...")
                    inventory.remove(items_dictionary[consumed_item])
                    character.consuming(consumed_item)
                    print(f"Your inventory consists of a " + ', '.join(inventory))
                    time.sleep(2)
                    movingcharacter()
               elif "exit" in edible_items:
                    movingcharacter()
               else:
                    print("Thats not an option")                   

character = Character(100, True, 10, 100, 0, 0, 100, 10, 3, world_map= world_map)

#Gameplay
def dametime():
          print("20 years ago...")
          print("KING: GRAB THEM! GRAB THEM ALL! DON'T LET ANY OF THESE FILTHY PEASANTS GET AWAY!")
          time.sleep(3)
          print(f"KNIGHTS: COME HERE YOU PILE OF FILTH. \x1B[3m{namechosen} gets grabbed\x1B[23m")
          time.sleep(3)
          print(f"{namechosen.upper()}'s MOTHER: NOO! LEAVE {namechosen.upper()} ALONE! ") 
          time.sleep(1.5)        
          print(f"\x1B[3mKnight aggresively drops {namechosen} and grabs the mother\x1B[23m")
          time.sleep(2)
          print(f"{namechosen.upper()}: MOTHER NOOOO!")
          time.sleep(1)
          print(f"{namechosen.upper()}'s MOTHER: Don't worry my child... you... shall... be king one day...")
          input("Press Enter to Continue: ")
          clear()
          print("PRESENT DAY...")
          print(f"""\x1B[3mAs {namechosen}'s mother was taken away to be killed by the king 20 years ago. \x1B[23m
The words of {namechosen}'s mother had always had a place in his heart. 
{namechosen} promised... he will become the king of the castle. 
After years of training and preparation and drawing out a map and plan to acheive his goal. 
He was finally ready. \x1B[23m""")
          input("Press Enter to continue into game: ")
          clear()
          print(f"You are in the game {namechosen}")
          inventory_function("knife")
          movingcharacter()

def movingcharacter():
          while character.is_alive == True: 
               print(f"Your status is currently: Health={character.health}, Power={character.power}, Money={character.money}, MaxHealth={character.max_health}, Stamina={character.stamina}, Hunger={character.hunger}") 
               options = input("Select one of the following commands:\nshowmap move inventory eat exit\nChoice: ").strip().lower()   
               if "inventory" in options:
                    print(f"This is your current inventory {inventory}") 
               elif "eat" in options:
                    consuming_food()
               elif "showmap" in options:
                    print_world_map(world_map,character)
               elif "move" in options:
                    direction = input("Where do you want to move? (north, south, east, west, or type 'exit' to stop): ").lower().strip()
                    if "exit" in direction:
                         movingcharacter()
                    elif direction in ["north", "south", "east", "west"]:
                         character.movement(direction)
                         current_cell = world_map.get_cell(character.x, character.y)
                         if current_cell.area.name == "Barren Land":
                              collect_items_barren_land(character, current_cell)
                              barren_enemy_detection(character, current_cell)
                         if current_cell.area.name == "Estate":
                              collect_items_estate(character, current_cell)
                         if current_cell.area.name == "Merchant_farm":
                              print("There is a merchant around here, good luck finding it")
                              collect_items_merchant_farm(character, current_cell)
                         if current_cell.area.name == "Village":
                              collect_items_village(character, current_cell)
                              village_enemy_detection(character, current_cell)
                         if current_cell.area.name == "Forest":
                              forest_enemy_detection(character, current_cell)
               
                    else:
                         print("Invalid direction. Please try again.")  
               elif "exit" in options:
                    quitting = input("Are you sure you would like to exit the game, if you type yes your progress will not be saved and you will exit or type no to cancel.") 
                    if quitting == "yes":
                         import sys
                         sys.exit("Exiting the game")
                    elif quitting == "no":
                         movingcharacter()
                    else:
                         print("That is an invalid option. Type either yes or no.")
               else:
                    print("This is not an option")

startermenu()
nameselection()
dametime()
