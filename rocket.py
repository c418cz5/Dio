# Academic Integrity Statement
# filename: rocket.py
# author: Rick
# student ID: 523588
# email: 1477624023@qq.com
# date: 24 November 2025
# description:
# This is my own work as defined by the Academic Integrity Policy of the University.

class Rocket:
    def __init__(self, damage: float) -> None:
     self._damage = 0.0
     self.set_damage(damage) 

    @property
    def damage(self) -> float:
       return self._damage
    
    @damage.setter
    def damage(self, damage: float) -> None:
       self.set_damage(damage)

    def set_damage(self, damage: float) -> None:
       if isinstance(damage, (int, float)) and damage >= 0.0:
            self._damage = float(damage)
        else:
            print("Error: Rocket damage must be a non-negative number")

    def __str__(self) -> str:
       return "Rocket(damage={:.1f})".format(self._damage)

    def __repr__(self) -> str:
       return "Rocket(damage={:.1f})".format(self._damage)
    
    