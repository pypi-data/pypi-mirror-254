import math

def area(radius):
    '''计算圆的面积'''
    return math.pi * radius ** 2
 
def perimeter(radius):
    '''计算圆的周长'''
    return 2 * math.pi * radius
 
def circumscribed_square_area(radius):
    """计算外接正方形的面积"""
    return (2 * radius) ** 2
 
def inscribed_square_area(radius):
    """计算内切正方形的面积"""
    return (2 * radius * math.sqrt(2)) ** 2 / 2