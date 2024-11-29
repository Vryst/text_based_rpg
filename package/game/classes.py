

import os

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
        
    def Attack(attacker, target):
        os.system("clear")
        if target.health <= 0:
            print(f"{target.name} sudah mati :v")
            
            pass
            
        else:
            target.health -= attacker.attack
            
            os.system("clear")
            
            print(f"{attacker.name} HP = {attacker.health}\n{target.name} HP = {target.health}")
            print(f"\n\n{attacker.name} telah memberikan damage {attacker.attack} ke {target.name}")
            
    def guard(self):
        self.guard = True
        
    def run():
    	return (True if random(range(1,10)) > 1 else False)