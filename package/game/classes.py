import json
import random
import os
import sys
from time import *
from datetime import datetime


def dash(n=25):
    print("-"*n)
    
    
def loading(duration=3):
    end_time = time() + duration  # Time duration for the animation
    
    frames = [
        "⠂⠄⠅","⠇⠆⠘","⠐⠠⠐",
        "⠄⠅⠇","⠆⠘⠐","⠠⠐⠘",
        "⠅⠇⠆","⠘⠐⠠","⠐⠘⠂",
        "⠇⠆⠘","⠐⠠⠐","⠘⠂⠄",
        "⠆⠘⠐","⠠⠐⠘","⠂⠄⠅",
        "⠘⠐⠠","⠐⠘⠂","⠄⠅⠇",
        "⠐⠠⠐","⠘⠂⠄","⠅⠇⠆",
        "⠠⠐⠘","⠂⠄⠅","⠇⠆⠘",
        "⠂⠄⠅","⠇⠆⠘","⠐⠠⠐"
    ]
    
    while time() < end_time:
        for frame in frames:
            if time() == end_time:
                break
            sys.stdout.write(f'\r{frame*10}')  # \r to overwrite the line
            sys.stdout.flush()  # Flush the output buffer
            sleep(0.05)
    clear()

    # Final message after the loading is done
    # Overwrite the loading text with "Done!"
    
    


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

roles_index = [
1,
2,
3,
4,
5,
6
]

#roles_index.append(len(roles_index)+1)
#print(roles_index)

roles = [
"warrior",
"archer",
"mage",
"thief",
"hero",
"bandit"
]

special_shop = [
"hero",
"thief",
"bandit",
"pirate"
]

musuh = [
"knight",
"skeleton",
"slime",
"tree",
"elmanuk",
"otong",
"jo",
"go",
"worga",
"ctulhu",
"jasendiri",
"zagon",
"cuda",
"loic",
"punda",
"vorhs",
"nokl",
"wryth"
]


#random picker
def randomizer(a=100):
    try:
            if type(a) == int:
                return random.choice(range(a))
            elif type(a) == list:
                return random.choice(a)
    except (TypeError, ValueError):
            print("\n\nMohon masukkan data dengan benar\n\n")


#percent
def percent(num=1):
        return num/100
        
        
#checking crit success
def critical(player):
    success = random.choice(range(1,100+1)) <= player.crate
    
    return success
    

#reducing input damage 
def attack_reduction(target,amount):
    
    
    
    if target.attack - amount <= 0:
        result = 0
        
        return result
    else:
        result = target.attack - amount
        return result
    


def get_loot(enemy):
    loot_table = {
        "serigala": [{"item": "Kulit Serigala", "chance": 0.8, "value": 5}],
        "naga": [
            {"item": "Taring Naga", "chance": 0.5, "value": 100},
            {"item": "Tulang Naga", "chance": 0.2, "value": 200}
        ]
    }
    loot = loot_table.get(enemy, [])
    dropped_items = []
    for item in loot:
        if random.random() < item["chance"]:
            dropped_items.append({"name": item["item"], "value": item["value"]})
    return dropped_items

#Contoh:
#loot = get_loot("naga")
#print(loot)  # Output: Drop acak dari loot naga


#============={{HERO}}===============
class Hero:
    
    def __init__(self,name=None,role=None,health=0,attack=0,defend=0,agility=0,crate=0,cdamage=0,coin=0,ctime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),guard=False,inventory=[],reputation=0):
        self.name = name
        self.role = role
        self.health = health
        self.attack = attack
        self.defend = defend
        self.agility = agility
        self.crate = crate
        self.cdamage = cdamage
        self.ctime = ctime
        self.guard = guard
        self.inventory = inventory
        self.coin = coin
        self.year = ctime[0:4]
        self.month = ctime[5:7]
        self.day = ctime[8:10]
        self.hour = ctime[11:13]
        self.minute = ctime[14:16]
        self.second = ctime[17:19]
        if role == "hero":
            
            self.reputation = 100
        else:
            self.reputation = reputation
        
    
    def __repr__(self):
        return (f"Hero(name={self.name}, role={self.role}, hp={self.health}, attack={self.attack}, "
                f"defend={self.defend}, agility={self.agility}, crit_rate={self.crate}, "
                f"crit_damage={self.cdamage}), created_time={self.ctime}")
                
                
    def __str__(self):
        
        print(f"""
        =====CHAR INFO=====
        Date created:
            Year   : {self.year}
            Month  : {self.month}
            Day    : {self.day}
            Hour   : {self.hour}
            Minute : {self.minute}
            Second : {self.second}
            
        Name = {self.name}
        Class = {self.role}
        HP = {self.health}
        ATK = {self.attack}
        DEF = {self.defend}
        AGI = {self.agility}
        CRIT RATE = {self.crate}%
        CRIT DAMAGE = {int(self.cdamage*100)}%
        
        Inventory:
        
        """
        )
        self.getInv()
        return ""
    
    @classmethod
    def saveData(cls,self, filename):
        """
        Save data to a JSON file.
        
        Args:
        data (dict): The data to save, typically a dictionary.
        filename (str): The name of the file where data will be saved.
        
        Returns:
        None
        """
        try:
            data = dict(self.__dict__)
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4, default=str)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")
            
            
    @classmethod
    def loadData(cls, json_file):
        """Class method to load Hero data from a JSON file."""
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        for k in data['inventory']:
            print(k)
            
        return cls(
            name=data['name'],
            role=data['role'],
            health=data['health'],
            attack=data['attack'],
            defend=data['defend'],
            agility=data['agility'],
            crate=data['crate'],
            cdamage=data['cdamage'],
            guard=data['guard'],
            inventory=[i for i in data['inventory']],
            ctime=data['ctime'],
            reputation=data['reputation']
            
        )
    
    
    def clearInv(self):
        self.inventory = []
        print("Inventory set to ",self.inventory)
        
        
    def addInv(self,*item):
        for i in item:
            self.inventory.append(str(i))
        
    def getInv(self):
        c = 1
        l = [i for i in self.inventory]
        #for i in self.inventory:
#            l.append(i)
            
        for j in l:
            print("\t"+"  "+str(c)+") "+j)
            c+=1
        
    def getStat(self):
        print(f"""
        Name = {self.name}
        Class = {self.role}
        HP = {self.health}
        ATK = {self.attack}
        DEF = {self.defend}
        AGI = {self.agility}
        CRIT RATE = {self.crate}
        CRIT DAMAGE = {self.cdamage}
        """)
    def Attack(self, target):
        clear()
        
        total_damage = self.attack
        crit = critical(self)
        
        if target.health <=0 and self.health <= 0:
            print(f"{self.name} dan {target.name} telah mati\n")
            
        elif target.health <= 0:
            print(f"{target.name} sudah mati :v")
            print(f"{self.name} HP = {self.health}\n{target.name} HP = {target.health}")
            
            pass
            
        elif self.health <= 0:
            print(f"{self.name} sudah mati :v")
            print(f"{self.name} HP = {self.health}\n{target.name} HP = {target.health}")
            
            pass
            
        else:
            
            if target.guard == True:
                target.health -= attack_reduction(self,target.defend*2)
                
                target.guard = False
                
            else:
                
                if crit:
                    
                    total_damage += int(self.attack * self.cdamage)
                    target.health -= total_damage
                    
                    
                    
                else:
                    crit = False
                    target.health -= total_damage
            
            clear()
            
            #critical hit alert
            if crit:
                print(f"{self.name} CRITICAL HIT\n")
                
                
            print(f"{self.name} HP = {self.health}\n{target.name} HP = {target.health}")
            
            print(f"\n\n{self.name} telah memberikan damage {total_damage} ke {target.name}")
        total_damage = self.attack
            
    def Guard(self):
        self.guard = True
        print(f"Defend milik {self.name} telah meningkat 2x lipat!")
        
    def Run(self):
        return random.randint(1, 100) <= self.agility


class Enemy(Hero):
    
    pass
    
#a = Hero()
#Hero.saveData(a,"playerData/acapona.json")

class Item:
    
    def __init__(self, name, base_price, rarity):
        self.name = name
        self.base_price = base_price
        self.rarity = rarity
        self.current_price = base_price
    
    
    
    def update_price(self, quantity_sold):
        demand_factor = max(0.5, 1 - (quantity_sold * 0.1))
        self.current_price = round(self.base_price * demand_factor)
        
    
    #Template untuk update selanjutnya
    #equipment info
    #def getDetail(item,filepath):
#            
#            with open(filepath, "r") as file:
#                data = json.load(file)  # Membaca file JSON
#                # Iterasi untuk mendapatkan key dan value
#                print(f"""
#Item   : {item}
#Details:
#        Name: {data[item]['name']}
#        Price: {data[item]['price']}
#        Heal: {data[item]['heal']}
#        Buff: {data[item]['buff']}
#        Expired time: {data[item]['expire']}
#                    """)
# Contoh:
#taring_naga = Item("Taring Naga", 100, "Rare")
#taring_naga.update_price(quantity_sold=10)
#print(taring_naga.current_price)  # Output: Harga menurun berdasarkan jumlah penjualan

class Makanan(Item):
    buah = []
    with open("foods.json","r") as file:
            daftar_buah = json.load(file)
            buah.extend(daftar_buah.keys())

    def __init__(self,name,heal):
        
        super().__init__(name,base_price,rarity)
        self.name = name
        self.base_price = base_price
        self.current_price = base_price
        self.heal = heal
        self.rarity = rarity
        
    def __str__(self):
        print(f"{self.name} efek heal {self.heal}")
        
    
    
    @classmethod
    def getDaftarBuah(cls):
        index = 1
        print("\nDAFTAR BUAH\n=============")
        for i in cls.buah:
            print(f"{index:<2} {i}")
            index +=1
            
    
    @classmethod
    def getBuah(cls,index):
        
        try:
            if index <= 0:
                raise IndexError
                
            else:
                pass
                
            print(f"Buah yang diambil {cls.buah[index-1]}")
            return cls.buah[index-1]
            
        except IndexError as e:
            dash()
            print("Error:\n",e)
            dash()
            print("\nWe didn't have that kind of food :D")
            print("Food number ",index, "Not found\n")
            loading(1)
            
        
    @classmethod
    def getDetail(cls,buah):
            
            with open("foods.json", "r") as file:
                data = json.load(file)  # Membaca file JSON
                
                print(f"""
Item   : {buah}
Details:
        Name: {data[buah]['name']}
        Price: {data[buah]['price']}
        Heal: {data[buah]['heal']}
        Buff: {data[buah]['buff']}
        Expired time: {data[buah]['expire']}
                    """)
                    
                    
                    
