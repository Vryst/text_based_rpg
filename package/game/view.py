
import os
from classes import *
from fun import *

clear = os.system("clear")

            


def main():
    
    global hero_class
    global hero_name
    global hero
    
    elmanuk = pilih_role()
    hero_class = elmanuk[1]
    hero_name = elmanuk[0]
    
    if hero_class == "1":
       hero = Hero(hero_name,
       "warrior", # class
       1000, # hp
       130, # atk
       30, # def
       percent(15), # agi
       35, # c.rate
       percent(80) # c.dmg
       )
       
    if hero_class == "2":
       hero = Hero(
       hero_name,
       "mage",  # class
       400,     # hp
       270,     # atk
       15,      # def
       percent(10),  # agi
       10,      # c.rate
       percent(120)   # c.dmg
       )

    
    
    if hero_class == "3":
       hero = Hero(hero_name,
       "archer", # class
       700, # hp
       80, # atk
       25, # def
       percent(65), # agi
       50, # c.rate
       percent(100) # c.dmg
       )
    
    
    musuh = Hero("elmanuk",
    "warrior",
    1000,
    90,
    percent(20),
    percent(15),
    percent(35),
    percent(80)
    )
    
    
    encounter(hero,musuh)
    
    print("\n\napacoba")
    
    i = input("input apa saja untuk melanjutkan")
        
        
main()
