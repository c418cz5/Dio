# Academic Integrity Statement
# filename: artefact.py
# author: Rick
# student ID: 523588
# email: 1477624023@qq.com
# date: 24 November 2025
# description:
# This is my own work as defined by the Academic Integrity Policy of the University.


class Artefact:
    def __init__(self, name: str, value: int) -> None:
        self._name = ""  
        self._value = 0
        self.set_name(name)
        self.set_value(value)

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
     self.set_name(name)
    
    @property
    def value(self) -> int:
       return self._value

    @value.setter
    def value(self, value: int) -> None: 
      self.set_value(value)

    def set_name(self, name: str) -> None:
      if isinstance(name, str) and name.strip():
            self._name = name.strip()
      else:
            print("Error: Artefact name must be a non-empty string")
    
    def set_value(self, value: int) -> None:
        if isinstance(value, int) and value >= 0:
            self._value = value
        else:
            print("Error: Artefact value must be a non-negative integer")

    
    def __str__(self) -> str:
        return "Artefact(name='{}', value={})".format(self._name, self._value)

    def __repr__(self) -> str:
        return "Artefact(name='{}', value={})".format(self._name, self._value)
    

