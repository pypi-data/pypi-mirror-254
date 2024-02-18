import math

def calculate_base_radius(height, slant_height):
    """
    根据圆锥的高和斜高计算底面半径。
   
    参数:
    height (float): 圆锥的高
    slant_height (float): 圆锥的斜高
   
    返回:
    float: 底面半径
    """
    return math.sqrt(slant_height ** 2 - height ** 2)
 
def calculate_slant_height(radius, height):
    """
    根据圆锥的底面半径和高计算斜高。
   
    参数:
    radius (float): 圆锥的底面半径
    height (float): 圆锥的高
   
    返回:
    float: 斜高
    """
    return math.sqrt(radius ** 2 + height ** 2)
 
def calculate_volume(radius, height):
    """
    根据圆锥的底面半径和高计算体积。
   
    参数:
    radius (float): 圆锥的底面半径
    height (float): 圆锥的高
   
    返回:
    float: 圆锥体积
    """
    return (1 / 3) * math.pi * radius ** 2 * height
 
def calculate_surface_area(radius, slant_height):
    """
    根据圆锥的底面半径和斜高计算表面积。
   
    参数:
    radius (float): 圆锥的底面半径
    slant_height (float): 圆锥的斜高
   
    返回:
    float: 圆锥表面积
    """
    return math.pi * radius * (radius + slant_height)