
import random
import os



def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

roles = [
"warrior",
"archer",
"mage",
"thief",
"hero",
"bandit"
]
musuh = [
"knight",
"skeleton",
"slime",
"wood",
"elmanuk",
"otong"
]


#random picker
def randomizer(a=1000):
    try:
            if type(a) == int:
                return random.choice(range(a))
            elif type(a) == list:
                return random.choice(a)
    except:
            print("\n\nMohon masukkan data dengan benar\n\n")







class Hero:
    
    def __init__(self,name=None,role=None,health=None,attack=None,defend=None,agility=None,crate=None,cdamage=None):
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
                target.health -= self.attack - target.defend * 2
                
            else:
                target.health -= self.attack
            
            clear()
            
            print(f"{self.name} HP = {self.health}\n{target.name} HP = {target.health}")
            print(f"\n\n{self.name} telah memberikan damage {self.attack} ke {target.name}")
            print(f"\n{target.name} telah memberikan damage {target.attack} ke {self.name}")
            
    def guard(self):
        self.guard = True
        print(f"Defend milik {self.name} telah meningkat 2x lipat!")
        
    def run():
    	return (True if random(range(1,10)) > 1 else False)
    	
class Enemy(Hero):
    
    pass
    