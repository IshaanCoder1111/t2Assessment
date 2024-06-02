import os, time, random

inventory = []

#Adding a clear function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

#Loading Function
loading = ["Loading👑", "Loading.👑", "Loading..👑"]
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
            input("Press any key to continue")
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
     inventory.append(item_received.lower())
     print(f"Your inventory consists of a " + ', '.join(inventory))   

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

def print_world_map(world_map, character):
    for y in range(world_map.height):
        for x in range(world_map.width):
            cell = world_map.get_cell(x, y)
            if character.x == x and character.y == y:
                 print("P", end=" ")
            elif cell and cell.area:
                print(cell.area.name[0], end=' ')
            else:
                print('.', end=' ')
        print()

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

     def consuming(self, item):
          self.health += item.health
          self.power += item.power
          self.hunger -= item.hunger
          self.stamina += item.stamina
          if item.name in ["vegetable","meat", "bread", "medicine"]:
               print(f"The {item} has been removed from your inventory")
               inventory.remove(item)
               print(f"Stats after consuming {item.name} Power:{self.power}, Health:{self.health}, Stamina:{self.stamina}, Hunger:{self.hunger}")
          else:
               print(f"Stats after obtaining {item.name} Power:{self.power}, Health:{self.health}, Stamina:{self.stamina}, Hunger:{self.hunger}")
     
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
                cell = self.world_map.get_cell(self.x, self.y)
                if cell and cell.area:
                    if cell.area.name == "Ocean":
                        print("You have entered the ocean and died")
                        time.sleep(2)
                        self.is_alive = False
                        endgame()
                    if (self.x, self.y) == (11,4):
                         merchant()
                    else:
                        print(f"You move {direction} to the {cell.area.name}.")         
            else:
                print("You can't go that way.")
        else:
            print("Invalid direction.")
               
     def attacking(self):
          self.stamina -= 3
          self.hunger += 3
          hitormiss2 = random.randint(1,2)
          if hitormiss2 == 1:
            print(f"{namechosen} has missed their attack")
          if hitormiss2 == 2:
               print(f"{namechosen} has hit the {Enemy.enemy_name} for {self.power} damage")
               character.damage_taken(self.power)

     def damage_taken(self,damage):
          self.health -= damage
          self.status_check()

     def status_check(self):
          if self.health <= 0:
               print(f"{namechosen} has been vanquished")
               self.is_alive = False
               endgame()
          if self.health > 0:
               print(f"{namechosen} has {self.health} hearts left")


class Enemy(Entity):
     def __init__(self, health, is_alive, power, enemy_name, loot_options):
          super().__init__(health, is_alive, power)
          self.enemy_name = enemy_name
          self.loot_options = loot_options

     def check_status(self):
          if self.health <= 0:
               print(f"{self.enemy_name} has been vanquished")
               self.is_alive = False
               self.items_dropped()
          if self.health > 0:
               print(f"{self.enemy_name} has {self.health} hearts left")
                
     def attacking(self):
        hitormiss = random.randint(1,2)
        if hitormiss == 1:
            print(f"{self.enemy_name} has missed their attack")
        if hitormiss == 2:
            print(f"{self.enemy_name} has hit the {namechosen} for {self.power} damage")
            Character.damage_taken(self.power)
                       
     def damage_taken(self):
          self.health -= Character.power
          self.check_status()

     def items_dropped(self):
          global loot
          loot = random.choice(self.loot_options)
          input(f"Congratulations You Have Acquired The {loot} Item, press any key to continue")
          if loot == "Meat":
               inventory_function("Meat")             
          if loot == "Vegetable":
               inventory_function("Vegetable")              
          if loot == "Bread":
               inventory_function("Bread")
          if loot == "Coin":
               Character.money += coin.value
          if loot == "Sword":
               Character.consuming(item=sword)
               inventory_function("Sword")
          if loot == "Armour":
               Character.max_health = 200
               Character.consuming(item=armour)
               inventory_function("Armour")


tiger = Enemy(health=random.randint(25, 35), is_alive=True, power=10, enemy_name="Tiger", loot_options=["Nothing", "Meat"])
bear = Enemy(health=random.randint(15,25), is_alive=True, power=5, enemy_name="bear", loot_options=["Nothing", "Meat"])
citizen_names = ["Jack", "Fred", "Amelia"]
citizen = Enemy(health=5, is_alive=True, power=5, enemy_name= random.choice(citizen_names), loot_options=["Bread", "Vegetables", "Coin", "Nothing"])
knight = Enemy(health=80, is_alive=True, power=15, enemy_name="Knight", loot_options=["Armour", "Sword", "Helmet"])
noble = Enemy(health=200, is_alive=True, power=40, enemy_name="Noble", loot_options=["Land"])
king = Enemy(health=3000, is_alive=True, power=300, enemy_name="King", loot_options=["Crown", "Royal Mantle"])
    
     

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
sword = Item(50, 0, 0, 15, 0, "sword")
land = Item(0,0,0,50,0,"land ownership") 
wine = Item(1,-2,-1,5,-2,"wine")

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
    "wine": wine
}

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
          input("WELCOME TO THE MERCHANT!")
          character_choicemerchant = input("Would you like to 'buy', 'sell', or 'exit'?")
          if "sell" in character_choicemerchant.lower():
               while True:
                    clear()
                    print(f"Your inventory consists of a " + ', '.join(inventory))
                    item_sell = input("What would you like to sell, or would you like to exit selling").strip().lower()
                    if item_sell in inventory:
                         if item_sell in ["armour", "knife", "sword", "helmet"]:
                              print(f"Sorry you are not able to sell your {item_sell}")
                         else:          
                              inventory.remove(item_sell)
                              item_addvalue = items_dictionary[item_sell].value
                              Character.money += item_addvalue
                              print(f"You have successfully sold the {item_sell}")
                              print(f"Your inventory consists of a " + ', '.join(inventory))    
                              input("Press enter to continue: ")
                              break
                    elif "exit" in item_sell:
                         print("Exiting the selling area")
                         time.sleep(1.5)
                         break
                    else:
                         print(f"You don't currently have {item_sell}")
                         time.sleep(1.5)

          if "buy" in character_choicemerchant:
               while True:
                    print("These are our current items available")
                    print("Vegetable, Meat, Bread, Medicine")
                    item_buy = input("Based on these items what would you like to buy, or would you like to exit buying").strip().lower()
                    if item_buy == "medicine":
                         inventory_function("medicine")
                    if item_buy == "vegetable":
                         inventory_function("vegetable")
                    if item_buy == "meat":
                         inventory_function("meat")
                    if item_buy == "bread":
                         inventory_function("bread")
                    elif "exit" in item_buy:
                         print("Exiting the buying area")
                         time.sleep(1.5)
                         break
                    else:
                         print(f"{item_buy} is not currently in our store, sorry for the inconvenience")

          if "exit" in item_sell:
                    print("Exiting the merchant")
                    time.sleep(1.5)
                    clear()
                    movingcharacter()    

          else:
               print("Thats not an option")  
               time.sleep(1.5)                       
                      

character = Character(100, True, 10, 100, 0, 0, 100, 1, 1, world_map= world_map)

#Gameplay
def dametime():         
          print(f"You are in the game {namechosen}")
          inventory_function("Knife")
          character.consuming(item=knife)
          print(f"These are your stats currently {character.power}, {character.health}")
          movingcharacter()

def movingcharacter():
          while character.is_alive == True: 
               options = input("Select one of the following commands:\nshowmap move\nChoice: ").strip().lower()             
               if options == "showmap":
                    print_world_map(world_map,character)
               if options == "move":
                    direction = input("Where do you want to move? (north, south, east, west, or type 'exit' to stop): ").lower()
                    if "exit" in direction:
                         break
                    elif direction in ["north", "south", "east", "west"]:
                         character.movement(direction)
                         current_cell = world_map.get_cell(character.x, character.y)
                         if current_cell.area.name == "Barren Land":
                              collect_items_barren_land(character, current_cell)
                         if current_cell.area.name == "Estate":
                              collect_items_estate(character, current_cell)
                         if current_cell.area.name == "Merchant_farm":
                              collect_items_merchant_farm(character, current_cell)
                         if current_cell.area.name == "Village":
                              collect_items_village(character, current_cell)
                    else:
                         print("Invalid direction. Please try again.")  
               

startermenu()
nameselection()
dametime()
