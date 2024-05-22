import os, time, random

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
    input("Press Any Key To Continue!")
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
          if Character.is_alive == True:
               print("Finished Game")
          if Character.is_alive == False:
               print("You Lost")
          input("Press Any Key To Continue")
          exit()

def inventory_function():
     inventory.append(loot)
     print(f"Your inventory consists of a " + ', '.join(inventory))   

class Cell:
    def __init__(self):
        self.area = None

class Area:
    def __init__(self,name,description,coordinates):
        self.name = name
        self.description = description
        self.coordinates = coordinates

    def insidearea(self, x, y):
        return (x, y) in self.coordinates


class WorldMap:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.grid = [[Cell() for i in range(width)]for i in range(height)]

    def add_area(self, area):
        for x, y in area.coordinates:
            if 0 < x < self.width and 0 < y < self.height:
                self.grid[y][x].area = area

    def get_cell(self, x, y):
        if 0 < x < self.width and 0 < y < self.height:
            return self.grid[y][x]
        return None

Village_hut = Area("Village_hut","Your home.",[(2,2)])
Village = Area("Village","The home of the villagers.",[(2,3),(2,4),(2,5),(2,6),(2,7),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7)]) 
Ocean = Area("Ocean","Enter with the risk of death.",[(x, 1) for x in range(18)] + [(x, 18) for x in range(18)] + [(1, y) for y in range(1, 18)] + [(17, y) for y in range(1, 18)])#not finished
Castle = Area("Castle","King's home.",[(8,10),(8,11),(8,12),(8,13),(9,10),(9,11),(9,12),(9,13),(10,10),(10,11),(10,12),(10,13),(11,10),(11,11),(11,12),(11,13)]) 
Merchant_farm = Area("Merchant_farm","The farm of resources.",[(11,2),(12,2),(13,2),(14,2),(15,2),(16,2),(17,2),(18,2),(11,3),(12,3),(13,3),(14,3),(15,3),(16,3),(17,3),(18,3),(11,4),(12,4),(13,4),(14,4),(15,4),(16,4),(17,4),(18,4),(11,5),(12,5),(13,5),(14,5),(15,5),(16,5),(17,5),(18,5)]) 
Forest = Area("Forest","Enter at your own risk.",[(2,15),(2,16),(2,17),(3,15),(3,16),(3,17),(4,15),(4,16),(4,17),(5,15),(5,16),(5,17)]) 
Estate = Area("Estate","Home of the nobles.",[(16,13),(16,14),(16,15),(16,16),(16,17),(17,13),(17,14),(17,15),(17,16),(17,17),(18,13),(18,14),(18,15),(18,16),(18,17)]) 

world_map = WorldMap(19,18)

world_map.add_area(Village_hut)
world_map.add_area(Village)
world_map.add_area(Ocean)
world_map.add_area(Castle)
world_map.add_area(Merchant_farm)
world_map.add_area(Forest)
world_map.add_area(Estate)

def print_world_map(world_map):
    for y in range(world_map.height):
        for x in range(world_map.width):
            cell = world_map.get_cell(x, y)
            if cell and cell.area:
                print(cell.area.name[0], end=' ')
            else:
                print('.', end=' ')
        print()


class Character:

     def __init__(self, power, stamina, health, money, max_health, is_alive):
          self.power = 0
          self.stamina = 100
          self.health = 100
          self.hunger = 0
          self.money = 0
          self.max_health = 100
          self.is_alive = True

     def consuming(self):
          self.health += Item.health
          self.power += Item.power
          self.hunger -= Item.hunger
          self.stamina += Item.stamina
     
     def movement(self):
          self.stamina -= 3
          self.hunger += 3
               
     def attacking(self):
          self.stamina -= 3
          self.hunger += 3
          hitormiss2 = random.randint(1,2)
          if hitormiss2 == 1:
            print(f"{namechosen} has missed their attack")
          if hitormiss2 == 2:
               print(f"{namechosen} has hit the {Enemy.enemy_name} for {self.power} damage")
               Enemy.damage_taken(self.power)

     def damage_taken(self):
          self.health -= Enemy.power
          self.status_check()

     def status_check(self):
          if self.health <= 0:
               print(f"{namechosen} has been vanquished")
               self.is_alive = False
               endgame()
          if self.health > 0:
               print(f"{namechosen} has {self.health} hearts left")
     

class Item:
    def __init__(self, power, stamina, hunger, value, health):
        self.power = power
        self.stamina = stamina
        self.hunger = hunger 
        self.value = value
        self.health = health

class Bread(Item):
     def __init__(self, power, stamina, hunger, value, health):
          super().__init__(2, 2, -3, 0, 1)
          Character.consuming(Bread)

class Meat(Item):
     def __init__(self, power, stamina, hunger, value, health):
          super().__init__(2, 2, -5, 0, 2)
          Character.consuming(Meat)

class Knife(Item):
     def __init__(self, power, stamina, hunger, value, health):
          super().__init__(20, 0, 0, 5, 0)
          Character.consuming(Knife)

class Coin(Item):
     def __init__(self, power, stamina, hunger, value, health):
          super().__init__(0, 0, 0, 1, 0)   
          Character.money += self.value     

class Vegetable(Item):
     def __init__(self, power, stamina, hunger, value, health):
          super().__init__(0, 5 , -3, 0, 2)
          Character.consuming(Vegetable)

class Jewellery(Item):
     def __init__(self, power, stamina, hunger, value, health):
          super().__init__(0, 0, 0, 5, 0)          

class Wine_Glass(Item):
     def __init__(self, power, stamina, hunger, value, health):
          super().__init__(0, 0, 0, 5, 0)
          
class Medicine(Item):
     def __init__(self, power, stamina, hunger, value, health):
          super().__init__(0, 0, 0, 8, 20)

class Oil(Item):
     def __init__(self, power, stamina, hunger, value, health):
          super().__init__(0, 0, 0, 3, 0)

class Armour(Item):
     def __init__(self, power, stamina, hunger, value, health):
          Character.max_health = 200
          super().__init__(10, 0, 0, 30, 0)

class Sword(Item):
     def __init__(self, power, stamina, hunger, value, health):
          super().__init__(50, 0, 0, 0, 0)
          Character.consuming(Sword)

class Enemy:
     
     def __init__(self, enemy_name, health, power, loot_options):
          self.enemy_name = enemy_name
          self.health = health
          self.power = power 
          self.loot_options = loot_options
          self.is_alive = True

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
               Coin()
          if loot == "Sword":
               Sword()
               inventory_function()
          if loot == "Armour":
               Armour()
               inventory_function()

class Tiger(Enemy):    
     def __init__(self, enemy_name, health, power, loot_options):
          health = random.randint(25,35)
          super().__init__("Tiger", health, 10, ["Nothing", "Meat"])

class Bear(Enemy):
     def __init__(self, enemy_name, health, power, loot_options):
          super().__init__(Bear, 20, 5, ["Nothing", "Meat"])

class Citizen(Enemy):
     def __init__(self, enemy_name, health, power, loot_options):
          citizen_names = ["Jack", "Fred", "Amelia"]
          self.enemy_name = random.choice(citizen_names)
          super().__init__(enemy_name, 10, 5, ["Bread", "Vegetables", "Coin", "Nothing"])       

class Knight(Enemy):
     def __init__(self, enemy_name, health, power, loot_options):
          super().__init__(Knight, 80, 15, ["Armour", "Sword", "Helmet"])

class Noble(Enemy):
     def __init__(self, enemy_name, health, power, loot_options):
          super().__init__("Noble", 200, 40, ["Land"])

class King(Enemy):
     def __init__(self, enemy_name, health, power, loot_options):
          super().__init__(King, 3000, 300, ["Crown", "Royal Mantle"])
              
     def items_dropped(self):
          endgame()
          return super().items_dropped()
     

while True:
     inventory = []
     inventory.append("Knife")
     print(f"You are in the game {namechosen}")
     print(f"Your inventory consists of a " + ', '.join(inventory))    
     Knife()
     Character.movement()
