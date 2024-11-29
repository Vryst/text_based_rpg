
from classes import *
from view import *


def role_picked(role):
    
    if role == "1":
        return Hero(hero_name,100,10)
         
    if role == "2":
        return Hero(hero_name,50,20)
        
    if role == "3":
        return Hero(hero_name,70,15)
        

