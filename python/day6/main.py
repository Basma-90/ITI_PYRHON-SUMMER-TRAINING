from datetime import date
from abc import ABC, abstractmethod

class Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width
    def Calc_area(self):
        return self.length*self.width
    def Calc_perimeter(self):
        return 2*(self.length+self.width)

class Vehicle:
    def __init__(self,speed,distance):
        self.__speed=speed
        self.__distance=distance
    def get_speed(self):
        return self.__speed
    def set_speed(self,value):
        self.__speed=value
    def get_distance(self):
        return self.__distance
    def set_distance(self,value):
        self.__distance=value

class Calculator:
    def sum(self,*args):
        sum=0
        for arg in args:
            sum=sum+arg
        return sum
    def multiply(self,*args):
        mul=1
        for arg in args:
            mul=mul*arg
        return mul
    def minus(self,*args):
        res=args[0]
        for i in range(1, len(args)):
            res=res-args[i]
        return res
    def divide(self,*args):
        res=args[0]
        for i in range(1, len(args)):
            res=res/args[i]
        return res
class Human:

    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth
    
    def tell_age(self):
        return date.today().year-self.date_of_birth.year
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 0.5*3.14*(self.radius**2)
    def perimeter(self):
        return 2*3.14*self.radius

class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length**2
    def perimeter(self):
        return self.length*4
class Triangle(Shape):
    def __init__(self,height1,height2,height3):
        self.height1=height1
        self.height2=height2
        self.height3=height3
    def area(self):
        s=0.5*(self.height1+self.height2+self.height3)
        return ((s-self.height1)*(s-self.height2)*(s-self.height3))**0.5
    def perimeter(self):
        return self.height1+self.height2+self.height3
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,value):
        self.items.append(value)

    def is_empty(self):
        return len(self.items) == 0
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

stack1=Stack()
input_s=input()
stack1.push(8)
stack1.push(9)
print(stack1.pop())
human1=Human('basma','egypt',date(2000,9,9))
print(human1.tell_age())









