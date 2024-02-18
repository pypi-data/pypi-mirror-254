import math
from   .. draw  import  draw2d


def is_valid(a, b, c):
    """检查这些边是否构成一个有效的三角形"""
    return a + b > c and a + c > b and b + c > a

def perimeter(a, b, c):
    """计算三角形的周长"""
    return a + b + c

def area(a, b, c):
    """用赫伦公式计算三角形的面积"""
    if is_valid(a, b, c):
        s = perimeter(a, b, c) / 2

        # 画出所求面积
        draw2d.draw_polygon([(0, 0), (a, 0), (0, b)], show_axes=True)

        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        raise ValueError("Invalid triangle sides")