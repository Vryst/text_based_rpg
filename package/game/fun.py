
import random
import os
from time import *
from classes import *

def maintenance():
    print("Fitur maintenance! :v")
    sleep(1)

def create_hero(hero_name, hero_class):
    roles = [
       #("role",   HP   ATK  DEF AGI CRATE CDMG)
        ("warrior", 1000, 130, 30, 15, 35, 80),
        ("mage", 400, 270, 15, 10, 10, 120),
        ("archer", 700, 80, 25, 45, 50, 100),
        ("hero", 2000, 100, 70, 10, 30, 100, 100),
        ("thief", 450, 50, 15, 70, 75, 200),
        ("bandit", 900, 95, 20, 5, 25, 70)
    ]
    
    role, health, attack, defend, agility, crit_rate, crit_dmg = roles[hero_class - 1]
    return Hero(hero_name, role, health, attack, defend, agility, crit_rate, percent(crit_dmg))
    
def main():
    clear()
    hero_name, hero_class = pilih_role()  # Pass directly
    hero = create_hero(hero_name, hero_class)

    
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
    
    

def battle(player,enemy):
            clear()
            print(f"Kamu bertarung melawan {enemy.name}!\n")
            
            while True:
                
                print(f"{player.name}'s HP: {player.health}")
                print(f"{enemy.name}'s HP: {enemy.health}")
                
                
                try:
                    
                    while True:
                        try:
                            print("""
Pilih aksi yang tersedia:
      1. Serang
      2. Bertahan
      3. Item
      4. Kabur\n""")
                            aksi_battle = int(input("Pilihan(1/2/3/4): "))
                            if aksi_battle in [1, 2, 3, 4]:
                                break  # Exit the loop if valid input is given
                            else:
                                clear()
                                print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
                                sleep(1)
                        except ValueError:
                            clear()
                            print("Harap masukkan angka yang valid (1/2/3/4).")
                            sleep(1)
        
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
                        
                        if enemy.health <= 0:
                            break
                        elif player.health <= 0:
                            break
                        try:
                            kabur = player.Run()
                            if kabur:
                                print("kamu kabur")
                                sleep(1)
                                break
                            else:
                                print("gagal")
                                sleep(1)
                                clear()
                        except TypeError:
                            print("Easter egg! :D")
                            
                    else:
                        clear()
                        pass
                except ValueError:
                    clear()
                    print("Harap masukkan input yang valid(1/2/3/4)!\n")
            if player.health <= 0:
                return False
                
            if enemy.health <= 0:
                
                return True
            
            else:
                return "kabur"

#event
def pergi():
    menemukan = random.choice(range(2))
    return 1 if menemukan == 1 else 2
    
    

    
#encounter
def encounter(hero):
    
    berjalan = pergi()
    enemy = Enemy(randomizer(musuh),randomizer(roles),randomizer(),randomizer(),randomizer(),randomizer(),randomizer(),randomizer())
    
    enemy.getStat()
    
    on = True
    if berjalan == 1:
       while on:
        
        lanjut = input("Serang? (y/n) : ").lower()
        
        if lanjut == "y":
                  hasil_pertarungan = battle(hero,enemy)
                  if hasil_pertarungan == "kabur":
                      print("\nKamu berhasil melarikan diri")
                      sleep(1)
                      break
                  if hasil_pertarungan == True:
                      print(f"\nKamu mengalahkan {enemy.name}!")
                      sleep(1)
                      break
                  else:
                      print("Game over")
                      sleep(1)
                      break
        if lanjut == 'n':
            print(f"\nKamu menghiraukan {enemy.name}\n\n")
            enemy = None
            sleep(1)
            break
     
    if berjalan == 2:
        shop(hero)
        clear()
        
    else:
        clear()
        print("Kamu berjalan tanpa arah")

#shop
def shop(player):
    clear()
    print(f"Selamat datang di toko, orang asing! heheh..\n")
    
    
    
    
    if player.role == "thief":
        print(f"\n0)Mencuri? :v")
        pass
    
    
    if player.role == "bandit":
        print(f"\n0)Rampok? :v")
        pass
    
    
    if player.role == "hero":
        print(f"\n0)Tunjukkan jasa?(menyombongkan diri dengan poin reputasi)\nPoin reputasi: {player.reputasi}:v")
        pass
    
    
    
    print("1)Beli\n2)Jual\n3)Pergi")
    
    aksi = True
    
    while aksi:
        
        try:
            global pilihan
            pilihan = int(input("\nPilih(1,2,3) : "))
        except ValueError:
            print("Apakah kau bisa baca oh orang asing?")
            sleep(1)
            
            pass
            
        if pilihan == 0:
            maintenance()
            break
    
        if pilihan == 1:
            maintenance()
            break
            
        if pilihan == 2:
            maintenance()
            break
        
        if pilihan == 3:
            aksi = False
            
#foods effect
def Apple(p):
    p.health += 10
    print("\nIts freshness helps you on adventure :D\n")
    print(f"""
    Temporary buff added:
        1. Bullseye (Crit Rate & Damage +5%)
        """)
    #maintenanced feature
    
#eating items
def eat(player,item):
    #on maintenance
    if item not in foods:
        print("You can't eat that :D")
    else:
        
        if item == "Apple":
            Apple(player)
            
        
        