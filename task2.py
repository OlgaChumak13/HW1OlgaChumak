import abc

# Define an abstract base class 'Shape' using the abc module
class Shape(object):
    __metaclass__= abc.ABCMeta
    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return

# Define a class 'Triangle' that inherits from 'Shape'
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.__a = a #creating encapsulation
        self.__b = b
        self.__c = c

    def set_size (self, a, b, c): # made function for setting size
        # condition that only numbers can be entered to avoid errors
        if type(a) in (int, float) and type(b) in (int, float) and type(c) in (int, float):
          self.__a = a
          self.__b = b
          self.__c = c

    def calc_perimeter(self):
        perim = self.__a + self.__b + self.__c
        print("Consider me implemented", perim)
        return perim



# Define a class 'Rectangle' that inherits from 'Shape'
class Rectangle(Shape):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def set_size (self, a, b): # made function for setting size
        # condition that only numbers can be entered to avoid errors
        if type(a) in (int, float) and type(b) in (int, float):
          self.__a = a
          self.__b = b

    def calc_perimeter(self):
        perim = 2 * (self.__a + self.__b)
        print("Consider me implemented", perim)
        return perim

# Define a class 'Square' that inherits from 'Rectangle'
class Square(Rectangle):
    def __init__(self, a):
        # Initialize the square using the side length for both sides of the rectangle
        super().__init__(a, a)
        self.__a = a
    def set_size (self, a): # made function for setting size
        # condition that only numbers can be entered to avoid errors
        if type(a) in (int, float):
          self.__a = a

    def calc_perimeter(self):
        perim = 4 * self.__a
        print("Consider me implemented", perim)
        return perim

# Create instances of each class

triangle_red = Triangle(0,0,0)
triangle_red.set_size(10,10,10,)
triangle_red.calc_perimeter()

rectangle_red = Rectangle(0,0)
rectangle_red.set_size(10,20)
rectangle_red.calc_perimeter()

square_red = Square(0)
square_red.set_size(10)
square_red.calc_perimeter()