# Academic Integrity Statement
# filename: ship.py
# author: Rick
# student ID: 523588
# email: 1477624023@qq.com
# date: 24 November 2025
# description:
# This is my own work as defined by the Academic Integrity Policy of the University.


from movable_object import MovableObject
from artefact import Artefact
from rocket_launcher import RocketLauncher
from rocket import Rocket

class Ship(MovableObject):
    def __init__(self, name: str, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)
        self._name = ""
        self._artefacts = []  
        self._rocket_launcher = RocketLauncher()
        self.set_name(name)

    @property
    def name(self) -> str:
         return self._name
     @name.setter
    def name(self, name: str) -> None:
      self.set_name(name)

    @property
    def artefacts(self) -> list[Artefact]:
        return self._artefacts.copy()  
    @property
    def rocket_launcher(self) -> RocketLauncher:
        return self._rocket_launcher

    def set_name(self, name: str) -> None:
        if isinstance(name, str) and name.strip():
            self._name = name.strip()
        else:
            print("Error: Ship name must be a non-empty string")

    def add_artefact(self, artefact: Artefact) -> None:
        if isinstance(artefact, Artefact):
            if len(self._artefacts) < 20:
                self._artefacts.append(artefact)
                print("Added {} to ship".format(artefact))
            else:
                print("Error: Ship can only store up to 20 artefacts")
        else:
            print("Error: Can only add Artefact objects to ship")

    def remove_artefact(self, artefact: Artefact) -> None:
        if artefact in self._artefacts:
            self._artefacts.remove(artefact)
            print("Removed {} from ship".format(artefact))
        else:
            print("Error: Artefact not found in ship")

    def get_artefact_value(self) -> int:
        total = sum(artefact.value for artefact in self._artefacts)
        print("Total artefact value on ship: {}".format(total))
        return total

    def fire_rocket(self) -> float | None:
        return self._rocket_launcher.fire()

    def reload_rocketlauncher(self, rocket: Rocket) -> None:
        self._rocket_launcher.reload_rocketlauncher(rocket)

    def __str__(self) -> str:
        return "Ship(name='{}', x={}, y={}, artefacts_count={}, rocket_launcher={})".format(
            self._name, self.x, self.y, len(self._artefacts), self._rocket_launcher
        )

    def __repr__(self) -> str:
        return "Ship(name='{}', x={}, y={}, artefacts={}, rocket_launcher={})".format(
            self._name, self.x, self.y, repr(self._artefacts), repr(self._rocket_launcher)
        )





    

    

