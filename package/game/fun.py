
import random
import os
from time import *
from classes import *

def maintenance():
    print("Fitur maintenance! :v")
    sleep(1)

def main():
    
    clear()
    
    global hero_class
    global hero_name
    global hero
    
    
    
    elmanuk = pilih_role()
    hero_class = elmanuk[1]
    hero_name = elmanuk[0]
    
    if hero_class == 1:
       hero = Hero(hero_name,
       "warrior", # class
       1000, # hp
       130, # atk
       30, # def
       15, # agi
       35, # c.rate
       percent(80) # c.dmg
       )
       
    if hero_class == 2:
       hero = Hero(
       hero_name,
       "mage",  # class
       400,     # hp
       270,     # atk
       15,      # def
       10,  # agi
       10,      # c.rate
       percent(120)   # c.dmg
       )

    
    
    if hero_class == 3:
       hero = Hero(hero_name,
       "archer", # class
       700, # hp
       80, # atk
       25, # def
       45, # agi
       50, # c.rate
       percent(100) # c.dmg
       )
    
    
    
    if hero_class == 4:
       hero = Hero(hero_name,
       "hero", # class
       2000, # hp
       100, # atk
       70, # def
       10, # agi
       30, # c.rate
       percent(100), # c.dmg
       100
       )
    
    
    
    if hero_class == 5:
       hero = Hero(hero_name,
       "thief", # class
       450, # hp
       50, # atk
       15, # def
       70, # agi
       75, # c.rate
       percent(200) # c.dmg
       )
    
    
    
    if hero_class == 6:
       hero = Hero(hero_name,
       "bandit", # class
       900, # hp
       95, # atk
       20, # def
       5, # agi
       25, # c.rate
       percent(70) # c.dmg
       )
    
    
    
    
    while True:
        encounter(hero)
        
        
        i = input("input apa saja untuk melanjutkan")        
    
    
    
    



#pilih role
def pilih_role():
    
    print(f"Selamat datang di Athanor :v\n\n\n")
    
    hero_name = str(input("masukkan nama hero: "))
    while True:
        try:
            hero_class = int(input("\npilih role :\n 1. Warrior\n 2. Mage\n 3. Archer\n 4. Hero\n 5. Thief\n 6. Bandit\n\npilihan: "))
            
            if hero_class in roles_index:
                break
            else:
                pass
                
        
        
        except:
            print("Harap pilih role yang tersedia!")
            pass
        
        
    return hero_name, hero_class
    
    



#percent
def percent(num=1):
        return num/100
        



def battle(player,enemy):
            clear()
            print(f"Kamu bertarung melawan {enemy.name}!\n")
            
            while True:
                
                print("""
Pilih aksi yang tersedia:
      1. Serang
      2. Bertahan
      3. Item
      4. Kabur\n""")
                try:
                    aksi_battle = int(input("Pilihan(1/2/3/4): "))
                    
                    if aksi_battle == 1:
                        player.Attack(enemy)
                        sleep(1)
                        enemy.Attack(player)
                        sleep(1)
                        
                    if aksi_battle == 2:
                        clear()
                        player.Guard()
                        
                        sleep(1)
                        enemy.Attack(player)
                        sleep(1)
                        
                        pass
                        
                    if aksi_battle == 3:
                        clear()
                        
                        while True:
                            
                            try:
                            
                                print(player.inventory)
                                pilih_item = int(input("Pilih item yang ingin digunakan: "))
                                #fungsi_item
                                maintenance()
                                
                                break
                            except ValueError:
                                clear()
                                print("Harap masukkan index yang valid!")
                                sleep(1)
                                pass
                    if aksi_battle == 4:
                        kabur = player.Run()
                        try:
                            if kabur:
                                print("kamu kabur")
                                sleep(1)
                                break
                            else:
                                print("gagal")
                                sleep(1)
                        except TypeError:
                            kabur = float(kabur)
                            
                    else:
                        clear()
                        pass
                except ValueError:
                    clear()
                    print("Harap masukkan input yang valid(1/2/3/4)!\n")


#event
def pergi():
    menemukan = random.choice(range(2))
    return 1 if menemukan == 1 else 2
    
    

    
#encounter
def encounter(hero):
    
    
    enemy = Enemy(randomizer(musuh),randomizer(roles),randomizer(),randomizer(),randomizer(),randomizer(),randomizer(),randomizer())
    
    enemy.getStat()
    
    on = True
    if pergi() == 1:
       while on:
        
        lanjut = input("Serang? (y/n) : ").lower()
        
        if lanjut == "y":
                  hasil_pertarungan = battle(hero,enemy)
                  if hasil_pertarungan == True:
                      print("\nKamu mengalahkan {enemy.name}!")
                      break
                  else:
                      print("Game over")
                      break
        if lanjut == 'n':
            print(f"\nKamu menghiraukan {enemy.name}\n\n")
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
        print(f"\n0)Mencuri? :v")
        pass
    
    
    if player.role == "bandit":
        print(f"\n0)Rampok? :v")
        pass
    
    
    if player.role == "hero":
        print(f"\n0)Tunjukkan jasa?(menyombongkan diri dengan poin reputasi)\nPoin reputasi: {player.reputasi}:v")
        pass
    
    
    
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
            
 