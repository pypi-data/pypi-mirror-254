import math

def calculate_volume(radius, height):
    """
    计算圆柱体的体积
 
    参数:
    radius (float): 圆柱体的底面半径
    height (float): 圆柱体的高
 
    返回:
    float: 圆柱体的体积
    """
    return math.pi * (radius ** 2) * height
 
def calculate_surface_area(radius, height):
    """
    计算圆柱体的表面积
 
    参数:
    radius (float): 圆柱体的底面半径
    height (float): 圆柱体的高
 
    返回:
    float: 圆柱体的表面积
    """
    return (2 * math.pi * radius * height) + (2 * math.pi * (radius ** 2))
 
def calculate_base_area(radius):
    """
    计算圆柱体底面的面积
 
    参数:
    radius (float): 圆柱体的底面半径
 
    返回:
    float: 圆柱体底面的面积
    """
    return math.pi * (radius ** 2)
 
def calculate_lateral_surface_area(radius, height):
    """
    计算圆柱体的侧面积
 
    参数:
    radius (float): 圆柱体的底面半径
    height (float): 圆柱体的高
 
    返回:
    float: 圆柱体的侧面积
    """
    return 2 * math.pi * radius * height