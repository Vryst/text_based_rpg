
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
"mage"
]
musuh = [
"knight",
"skeleton",
"slime",
"wood"
]





def randomizer(a=100):
    try:
            if type(a) == int:
                return random.choice(range(a))
            elif type(a) == list:
                return random.choice(a)
    except:
            print("\n\nMohon masukkan data dengan benar\n\n")
            



class Hero:
    
    def __init__(self,name=randomizer(musuh),role=randomizer(roles),health=randomizer(),attack=randomizer(),defend=randomizer(),agility=randomizer(),crate=randomizer(),cdamage=randomizer()):
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
    def Attack(attacker, target):
        clear()
        
        if target.health <=0 and attacker.health <= 0:
            print(f"{attacker.name} dan {target.name} telah mati\n")
            
        elif target.health <= 0:
            print(f"{target.name} sudah mati :v")
            print(f"{attacker.name} HP = {attacker.health}\n{target.name} HP = {target.health}")
            
            pass
            
        elif attacker.health <= 0:
            print(f"{attacker.name} sudah mati :v")
            print(f"{attacker.name} HP = {attacker.health}\n{target.name} HP = {target.health}")
            
            pass
            
        else:
            target.health -= attacker.attack - (target.defend * 2 if attacker.guard == True else target.defend)
            
            clear()
            
            print(f"{attacker.name} HP = {attacker.health}\n{target.name} HP = {target.health}")
            print(f"\n\n{attacker.name} telah memberikan damage {attacker.attack} ke {target.name}")
            print(f"\n{target.name} telah memberikan damage {target.attack} ke {attacker.name}")
            
    def guard(self):
        self.guard = True
        print(f"Defend milik {self.name} telah meningkat 2x lipat!")
        
    def run():
    	return (True if random(range(1,10)) > 1 else False)
    	
class Enemy(Hero):
    
    pass
    
#manuk = Enemy(randomizer(musuh))

#manuk.getStat()