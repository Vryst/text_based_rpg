

from classes import *

def maintenance():
    print("Fitur maintenance! :v")
    loading(1)



def create_hero(hero_name, hero_class):
    roles = [
       #("role",   HP   ATK  DEF AGI CRATE CDMG)
        ("warrior", 1000, 130, 30, 15, 35, 80),
        ("mage", 400, 270, 15, 10, 10, 120),
        ("archer", 700, 80, 25, 45, 50, 100),
        ("hero", 2000, 100, 70, 10, 30, 100),
        ("thief", 450, 50, 15, 70, 75, 200),
        ("bandit", 900, 95, 20, 5, 25, 70)
    ]
    
    role, health, attack, defend, agility, crit_rate, crit_dmg = roles[hero_class - 1]
    return Hero(hero_name, role, health, attack, defend, agility, crit_rate, percent(crit_dmg))
    



        


def main(load=False):
    clear()
    if load == False:
        hero_name, hero_class = pilih_role()  # Pass directly
        hero = create_hero(hero_name, hero_class)
    elif load != False:
        hero = Hero.loadData(load)
        print(f"========LOADED CHAR========")
        hero.getStat()
        input("Input apa saja untuk melanjutkan\n")
        loading(0.5)
    
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
                                loading(1)
                        except ValueError:
                            clear()
                            print("Harap masukkan angka yang valid (1/2/3/4).")
                            loading(1)
        
                    if aksi_battle == 1:
                        player.Attack(enemy)
                        loading(1)
                        enemy.Attack(player)
                        loading(1)
                        
                    if aksi_battle == 2:
                        clear()
                        player.Guard()
                        
                        loading(1)
                        enemy.Attack(player)
                        loading(1)
                        
                        pass
                        
                    if aksi_battle == 3:
                        clear()
                        
                        while True:
                            
                            try:
                                a = 1
                                for i in player.inventory :
                                    print(f"{a}.{i}")
                                    a += 1
                                pilih_item = int(input("Pilih item yang ingin digunakan: "))
                                #fungsi_item
                                maintenance()
                                
                                break
                            except ValueError:
                                clear()
                                print("Harap masukkan index yang valid!")
                                loading(1)
                                
                    if aksi_battle == 4:
                        
                        if enemy.health <= 0:
                            break
                        elif player.health <= 0:
                            break
                        try:
                            kabur = player.Run()
                            if kabur:
                                print("kamu kabur")
                                loading(1)
                                break
                            else:
                                print("gagal")
                                loading(1)
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
    
    
    on = True
    if berjalan == 1:
       while on:
        
        enemy = Enemy(randomizer(musuh),randomizer(roles),randomizer(),randomizer(),randomizer(),randomizer(),randomizer(),randomizer())
        
        enemy.getStat()
        lanjut = input("Serang? (y/n) : ").lower()
        
        if lanjut == "y":
                  hasil_pertarungan = battle(hero,enemy)
                  if hasil_pertarungan == "kabur":
                      print("\nKamu berhasil melarikan diri")
                      loading(1)
                      break
                  if hasil_pertarungan == True:
                      print(f"\nKamu mengalahkan {enemy.name}!")
                      loading(1)
                      break
                  else:
                      print("Game over")
                      loading(1)
                      break
        if lanjut == 'n':
            print(f"\nKamu menghiraukan {enemy.name}\n\n")
            enemy = None
            loading(1)
            break
     
    if berjalan == 2:
        shop(hero)
        clear()
        
    else:
        clear()
        print("Kamu berjalan tanpa arah")



#special shop interaction checker
def isSpecialShop(player):
    if player.role == "thief":
        print(f"\n0)Mencuri? :v")
        pass
    
    
    if player.role == "bandit":
        print(f"\n0)Rampok? :v")
        pass
    
    
    if player.role == "hero":
        print(f"\n0)Tunjukkan jasa?\n(menyombongkan diri dengan poin reputasi)\n\nPoin reputasi: {player.reputation}:v")
        pass
        
    else:
        pass
        
#shop
def shop(player):
    
    aksi = True
    
    pilihan = None
    while aksi:
        clear()
        print(f"Selamat datang di toko, orang asing! heheh..\n")
        isSpecialShop(player)
        print("1)Beli\n2)Jual\n3)Pergi")
        try:
            
            pilihan = int(input("\nPilih(1,2,3) : "))
            if pilihan not in [0,1,2,3,4]:
                print("Harap masukkan pilihan yang tersedia! (1/2/3)")
                loading(1)
        except ValueError:
            print("Apakah kau bisa baca oh orang asing?")
            loading(1)
            
            
            
        if pilihan == 0:
            maintenance()
            break
    
        if pilihan == 1:
            buy(player)
            break
            
        if pilihan == 2:
            sell(player,item,jumlah)
            break
        
        if pilihan == 3:
            aksi = False
            
        else:
            pass
            
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
            
        

        
#buy


def buy(player):
    keranjang = []

    while True:
        print("""
apa yg ingin kamu beli
1.apple
""")
        beli = input("")
        keranjang.append(beli)
        for i in keranjang :
            print(f"- {i}")
        loading()
        keluar = input()
        if keluar == "y":
            pass
        if keluar == "n":
            break
    player.inventory += keranjang



def sell(player, item, jumlah):
        for i in player.inventory_list:
            if i.item == item:
                if player.stock >= jumlah:
                    hasil = barang.harga * jumlah * 80/100
                    player.stok -= jumlah
                    print(f"Transaksi berhasil: {jumlah} '{nama}'terjual.Total:{hasil}")
                    return
                else:
                    print(f"Stok '{nama}' tidak cukup.")
                    return
        print(f"Barang '{nama}' tidak ditemukan.")
        

