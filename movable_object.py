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
    

    @y.setter
    def y(self, y: int) -> None:
       self.set_y(y)

    def set_x(self, x: int) -> None:  
        if isinstance(x, int) and x >= 0:
            self._x = x
        else:
            print("Error: x coordinate must be a non-negative integer")


        
    def set_y(self, y: int) -> None:
        if isinstance(y, int) and y >= 0:
            self._y = y
        else:
            print("Error: y coordinate must be a non-negative integer")
        
    def move(self, dx: int, dy: int) -> None:
        new_x = self._x + dx
        new_y = self._y + dy
        if new_x >= 0 and new_y >= 0:
            self._x = new_x
            self._y = new_y
            print("Moved to x={}, y={}".format(new_x, new_y))
        else:
            print("Error: Move would result in negative coordinates")
    
    def __str__(self) -> str:
        return "MovableObject(x={}, y={})".format(self._x, self._y)

    def __repr__(self) -> str:
        return "MovableObject(x={}, y={})".format(self._x, self._y)



