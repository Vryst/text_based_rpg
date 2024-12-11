
import random
import os



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
    except:
            print("\n\nMohon masukkan data dengan benar\n\n")



def stat_reduction(target,amount):
    stat_now = target.attack
    
    
    if target.attack - amount <= 0:
        result = 0
        
        return result
    else:
        result = target.attack - amount
        return result
    
    

'''
class Dummy:
    def __init__(self,attack):
        self.attack = attack
        
dummy = Dummy(100)
print(dummy.attack)

if stat_reduction(dummy,50) ==
print(dummy.attack)
'''


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
        self.reputasi = reputasi
        
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
                target.health -= stat_reduction(self,target.defend*2)
                
                target.guard = False
                
            else:
                target.health -= self.attack
            
            clear()
            
            print(f"{self.name} HP = {self.health}\n{target.name} HP = {target.health}")
            print(f"\n\n{self.name} telah memberikan damage {self.attack} ke {target.name}")
            #print(f"\n{target.name} telah memberikan damage {target.attack} ke {self.name}")
            
    def Guard(self):
        self.guard = True
        print(f"Defend milik {self.name} telah meningkat 2x lipat!")
        
    def Run(self):
    	return True if random.choice(range(self.agility)) >= 1 else False


class Enemy(Hero):
    
    pass
    
    
'''
debug
a = Hero()
a.agility = randomizer()

k = a.run()
print(k)
'''