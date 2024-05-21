import os, time

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

class Enemy:
     
     def __init__(self, enemy_name, health, power, loot_options):
          self.enemy_name = enemy_name
          self.health = health
          self.power = power 
          self.loot_options = loot_options
          self.is_alive = True

     def check_status(self):
          if self.health >= 0:
               print(f"{self.enemy_name} has been vanquished")
               self.is_alive = False
               self.items_dropped()
          if self.health > 0:
               print(f"{self.enemy_name} has {self.health} hearts left")
                

     def attacking(self, main_player):
        hitormiss = random.randint(1,2)
        if hitormiss == 1:
            print(f"{self.enemy_name} has missed their attack")
        if hitormiss == 2:
            print(f"{self.enemy_name} has hit the {main_player} for {self.power} damage")
                       
    
     def damage_taken(self, attack_damage):
          self.health -= attack_damage
          self.check_status()

     def items_dropped(self, loot):
          loot = random.choice(self.loot_options)
          print(f"Congratulations You Have Acquired The {loot} Item")


class Tiger(Enemy):    
     def __init__(self, enemy_name, health, power, loot_options):
          super().__init__("Tiger", 30, 10, ["Nothing", "Meat", "Double Meat"])


class Bear(Enemy):
     def __init__(self, enemy_name, health, power, loot_options):
          super().__init__(Bear, 20, 5, ["Nothing", "Meat"])

class Citizen(Enemy):
     def __init__(self, enemy_name, health, power, loot_options):
          citizen_names = ["Jack", "Fred", "Amelia"]
          enemy_name = random.choice(citizen_names)
          super().__init__(enemy_name, 10, 5, ["Bread", "Vegetables", "$1", "$2", "Nothing"])       

class Knight(Enemy):
     def __init__(self, enemy_name, health, power, loot_options):
          super().__init__(Knight, 80, 15, None)

class Noble(Enemy):
     def __init__(self, enemy_name, health, power, loot_options):
          super().__init__("Noble", 200, 40, "Nothing")

class King(Enemy):
     def __init__(self, enemy_name, health, power, loot_options):
          super().__init__(King, 3000, 300, ["Crown", "Royal Mantle"])
    
     def items_dropped(self, loot):
          self.endgame()
          return super().items_dropped(loot)
     
     def endgame():
          clear()
          print("Placeholder For Finishing Game")
          input("Press Any Key To Continue")
          exit()
         
class Item:    
     def __init__(self, health, power, value):
          self.health = health
          self.power = power
          self.value = value


item1 - Item()
item1.name = "Coin"
item1.money = "1"
