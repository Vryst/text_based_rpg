

import os

clear = os.system("clear")

class Hero:
    
    def __init__(self,name,role,health,attack,defend,agility,crate,cdamage):
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
        
        
    def Attack(attacker, target):
        os.system("clear")
        if target.health <= 0:
            print(f"{target.name} sudah mati :v")
            
            pass
        if attacker.health <= 0:
            print(f"{attacker.name} sudah mati :v")
            
            pass
            
        else:
            target.health -= attacker.attack
            
            os.system("clear")
            
            print(f"{attacker.name} HP = {attacker.health}\n{target.name} HP = {target.health}")
            print(f"\n\n{attacker.name} telah memberikan damage {attacker.attack} ke {target.name}")
            print(f"\n{target.name} telah memberikan damage {target.attack} ke {attacker.name}")
            
    def guard(self):
        self.guard = True
        print(f"Defend milik {self.name} telah meningkat 2x lipat!")
        
    def run():
    	return (True if random(range(1,10)) > 1 else False)
