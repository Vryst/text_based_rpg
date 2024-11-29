
import os
from classes import *


clear = os.system("clear")

            

def percent(num=1):
        return num/100
        

print(f"Selamat datang di Athanor :v\n\n\n")
        
hero_name = str(input("masukkan nama hero: "))
hero_class = str(input("\npilih role :\n 1. Warrior\n 2. Mage\n 3. Archer\n\npilihan: "))

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
    hero = Hero(hero_name,
    "mage", # class
    400, # hp
    270, # atk
    15, # def
    percent(10), # agi
    10, # c.rate
    percent(120) # c.dmg
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


musuh = Hero("aob",
    "warrior",
    1000,
    130,
    percent(20),
    percent(15),
    percent(35),
    percent(80)
    )
on = True

while on:
    
    
    lanjut = input("Serang? (y/n) : ")
    
    if lanjut == "y" or "Y" or "Yes" or "yes" or "Ya" or "ya":
            
            if hero.health or musuh.health <= 0:
                pass
            
            
            hero.Attack(musuh)
            musuh.Attack(hero)
    elif lanjut == "n":
        
        on = False
        
        