import math
from  .. draw  import  draw3d

def calculate_volume(radius):
    """
    计算球体的体积。
 
    参数:
    radius (float): 球体的半径。
 
    返回:
    float: 球体的体积。
    """

    return (4.0/3.0) * math.pi * (radius ** 3)
 
def calculate_surface_area(radius):
    """
    计算球体的表面积。
 
    参数:
    radius (float): 球体的半径。
 
    返回:
    float: 球体的表面积。
    """
    draw3d.draw_3d_sphere(radius)
    return 4 * math.pi * (radius ** 2)
 
def is_point_inside_sphere(point, center, radius):
    """
    判断一个点是否在球体内。
 
    参数:
    point (tuple): 待判断的点的坐标。
    center (tuple): 球体中心的坐标。
    radius (float): 球体的半径。
 
    返回:
    bool: 如果点在球体内返回 True，否则返回 False。
    """
    squared_distance = sum((p - c) ** 2 for p, c in zip(point, center))
    return squared_distance <= radius ** 2