
import random
import os
import time
from classes import *




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
    
    
    
    
    while True:
        encounter(hero)
        
        
        i = input("input apa saja untuk melanjutkan")        
    
    
    
    



#pilih role
def pilih_role():
    
    print(f"Selamat datang di Athanor :v\n\n\n")
    
    hero_name = str(input("masukkan nama hero: "))
    hero_class = str(input("\npilih role :\n 1. Warrior\n 2. Mage\n 3. Archer\n\npilihan: "))
    
    return hero_name, hero_class



#percent
def percent(num=1):
        return num/100
        



            
            
            

#event
def pergi():
    menemukan = random.choice(range(1,2))
    return 1 if menemukan == 1 else 2
    
    
    
#encounter
def encounter(hero):
    
    
    enemy = Enemy(randomizer(musuh),randomizer(roles),randomizer(),randomizer(),randomizer(),randomizer(),randomizer(),randomizer())
    
    enemy.getStat()
    
    on = True
    if pergi() == 1:
       while on:
        
        lanjut = input("Serang? (y/n) : ")
        
        if lanjut == "y" or "Y" or "Yes" or "yes" or "Ya" or "ya":
                   
                   if hero.health or enemy.health <= 0:
                       
                       pass
                       
                       
                       
                       hero.Attack(enemy)
                       
                       enemy.Attack(hero)
                   if lanjut == "n":
                     print("Game berakhir :v")
                     enemy = None
                     break
     
    if pergi() == 2:
        shop(hero)
        
    else:
        clear()
        print("Kamu berjalan tanpa arah")

#shop
def shop(player):
    clear()
    print(f"Selamat datang di toko, orang asing! heheh..")
    
    
    
    if player.role == "thief":
        print("\n1)Beli\n2)Jual\n3)Mencuri? heheheh :v")
        pass
    
    
    if player.role == "bandit":
        print("\n1)Beli\n2)Jual\n3)Rampok? heheheh :v")
        pass
    
    
    if player.role == "hero":
        print("\n1)Beli\n2)Jual\n3)Tunjukkan jasa?(menyombongkan diri dengan poin reputasi) :v")
        pass
    
    
    else:
        print("\n1)Beli\n2)Jual\n3)Pergi")
    
    aksi = True
    
    while aksi:
        
        try:
            global pilihan
            pilihan = int(input("\nPilih(1,2,3) : "))
        except:
            pilihan = 0
            print("Apakah kau bisa baca oh orang asing?")
            #os.system("clear")
            pass
    
        if pilihan == 1:
            print("\n\nsedang maintenance, harap kembali beberapa hari kemudian :v\n\n")
            break
            
        if pilihan == 2:
            print("\n\nsedang maintenance, harap kembali beberapa hari kemudian :v\n\n")
            break
        
        if pilihan == 3:
            aksi = False
            
 