import math

def area(side):
    """计算正方形的面积"""
    return side * side
 
def perimeter(side):
    """计算正方形的周长"""
    return 4 * side
 
def diagonal(side):
    """计算正方形的对角线长度"""
    return math.sqrt(2) * side