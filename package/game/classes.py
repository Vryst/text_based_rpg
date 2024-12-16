import json
import random
import os
from time import sleep
from datetime import datetime



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
    
    

#============={{HERO}}===============
class Hero:
    
    def __init__(self,name=None,role=None,health=0,attack=0,defend=0,agility=0,crate=0,cdamage=0,ctime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),guard=False,inventory=[],reputation=0):
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
        self.year = ctime[0:4]
        self.month = ctime[5:7]
        self.day = ctime[8:10]
        self.hour = ctime[11:13]
        self.minute = ctime[14:16]
        self.second = ctime[17:19]
        if role == "hero":
            
            self.reputation = reputation
        else:
            self.reputation = 0
        
    
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

    def __init__(self,i):
        self.nama = i

class Makanan(Item):
    buah = []


    def __init__(self,i,heal):
        self.buah.append(i)
        super().__init__(i)
        self.heal = heal
    def __str__(self):
        print(f"{self.i} efek heal {self.heal}")

apple = Makanan("apple",10)
jeruk = Makanan("jeruk",15)
semangka = Makanan("semangka",30)
pisang = Makanan("pisang",20)

print(makanan.buah)


