#!/usr/bin/python3

class Square:

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise Typeerror("size must be an integer")
        elif size < 0:
            raise Valueerror("size must beb- => 0")
        else:
            self.__size = size
     
     def area(self):

         return self.__sizze ** 2
