
import random
import os
from time import sleep


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
    
    


class Hero:
    
    def __init__(self,name=None,role=None,health=None,attack=None,defend=None,agility=None,crate=None,cdamage=None,reputasi=0):
        self.name = name
        self.role = role
        self.health = health
        self.attack = attack
        self.defend = defend
        self.agility = agility
        self.crate = crate
        self.cdamage = cdamage
        self.guard = False
        self.inventory = []
        if role == "hero":
            
            self.reputation = reputasi
        else:
            self.reputation = 0
        
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
    
    

#debug
#hero = Hero("a",
#       "thief", # class
#       900, # hp
#       100, # atk
#       20, # def
#       5, # agi
#       100, # c.rate
#       percent(100) # c.dmg
#       )
#       
#monster = Enemy("b",
#       "bandit", # class
#       900, # hp
#       100, # atk
#       20, # def
#       5, # agi
#       100, # c.rate
#       percent(70) # c.dmg
#       )
#       
#hero.Attack(monster)
#sleep(1)
#monster.Attack(hero)
#print(hero.reputation)
