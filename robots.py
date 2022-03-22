

from robotsVSdinos.robotsVSdinos.weapons import Weapons


name = ['Mega Boss', 'Short Circuit', 'Iron Baby']
health = 100
weapon = Weapons

class Robots:
    def __init__(self, health, weapon):
        self.name = name       
        self.health = health
        self.weapon = weapon

    def attack(self, dinosaur): None    