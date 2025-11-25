# Academic Integrity Statement
# filename: movable_object.py
# author: Rick
# student ID: 523588
# email: 1477624023@qq.com
# date: 24 November 2025
# description:
# This is my own work as defined by the Academic Integrity Policy of the University.

class MovableObject:
    def _init_(self, x :int =0,y:int=0)->None:
        self._x =0
        self._y = 0
        self.set_x(x)
        self.set_y(y)

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        self.set_x(x)

    
    @property
     def y(self) -> int:
        return self._y
        
      


