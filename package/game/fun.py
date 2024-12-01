
import time
from classes import *



cls = os.system("clear")




def pilih_role():
    
    print(f"Selamat datang di Athanor :v\n\n\n")
    
    hero_name = str(input("masukkan nama hero: "))
    hero_class = str(input("\npilih role :\n 1. Warrior\n 2. Mage\n 3. Archer\n\npilihan: "))
    
    return hero_name, hero_class




def percent(num=1):
        return num/100
        



def encounter(hero,enemy):
    
    on = True
    
    while on:
        
        lanjut = input("Serang? (y/n) : ")
        
        if lanjut == "y" or "Y" or "Yes" or "yes" or "Ya" or "ya":
                   
                   if hero.health or enemy.health <= 0:
                       
                       pass
                       
                       hero.Attack(enemy)
                       
                       enemy.Attack(hero)
                   if lanjut == "n":
                       print("Game berakhir :v")
                       break




def shop(player,merchant):
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
			print("aku aob")
			cls
			break

map = {

"merchant" : "elmanuk"

}

'''p = Hero("Elmanuk",
    "hero", # class
    700, # hp
    80, # atk
    25, # def
    percent(65), # agi
    50, # c.rate
    percent(100) # c.dmg
    )'''
    
#shop(p,1)
