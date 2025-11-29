# Academic Integrity Statement
# filename: rocket_launcher.py
# author: Rick
# student ID: 523588
# email: 1477624023@qq.com
# date: 24 November 2025
# description:
# This is my own work as defined by the Academic Integrity Policy of the University.


from rocket import Rocket
class RocketLauncher:
    def __init__(self) -> None:
        self._rocket = None  # Holds 0 or 1 Rocket
    
    @property
    def rocket(self) -> Rocket | None:
        return self._rocket
    
    def reload_rocketlauncher(self, rocket: Rocket) -> None:
         if isinstance(rocket, Rocket):
            self._rocket = rocket
            print("RocketLauncher reloaded with {}".format(rocket))
        else:
            print("Error: Can only reload with a Rocket object")

    def fire(self) -> float | None:
         if self._rocket:
            damage = self._rocket.damage
            print("RocketLauncher fired {}".format(self._rocket))
            self._rocket = None  
            return damage
        else:
            print("Error: RocketLauncher is empty - cannot fire")
            return None

    def __str__(self) -> str:
         oaded_status = self._rocket if self._rocket else "empty"
        return "RocketLauncher(loaded={})".format(loaded_status)

    def __repr__(self) -> str:
         loaded_status = repr(self._rocket) if self._rocket else "None"
        return "RocketLauncher(loaded={})".format(loaded_status)


