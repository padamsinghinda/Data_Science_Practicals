# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 01:13:04 2017

@author: Padam Singh
"""

class Triangle :
    """
    This class accepts lenght of the sides of triangle as parameters.
    """
    def __init__(self, l1, l2, l3):
        self.side1 = l1
        self.side2 = l2
        self.side3 = l3
        
class Area(Triangle):    
    """
    This class inherits Triangle class and implements method to calculate area of the triangle.
    """    
    def triangle_area(self) :
        s = (self.side1 + self.side2 + self.side3)/2
        area = (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
        return area

def main():
    s1 = int(input("Enter side 1 : "))
    s2 = int(input("Enter side 2 : "))
    s3 = int(input("Enter side 3 : "))
    
    obj = Area(s1, s2, s3)
    output = obj.triangle_area()
    
    
    print("\nArea of triangle is : {}".format(output))
 
if __name__ == '__main__':
    main()