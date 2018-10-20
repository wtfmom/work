import math


class Rectangle(object):
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def area (self):
        return  self.a * self.b
    
class Square(Rectangle):
    def __init__(self, a=0):
        self.a=a
        self.b=a   
        
class Ellipse(object):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def area (self):
        return self.a * self.b * math.pi
    
class Circle(Ellipse):
    def __init__(self, r=0):
        self.a = r
        self.b = r
        
def compute_area(shapes):
        return sum(i.area() for i in shapes)

shapes=[Ellipse(10,20),Square(15),Circle(5)
        ,Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]
total_area=compute_area(shapes)
print(total_area)
