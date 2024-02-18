import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def draw_polygon(vertexes, color='red', show_axes=True):
    """绘制一个多边形，并可选地显示包含负坐标的坐标轴。
   
    参数:
    vertexes -- 一个列表，包含多边形顶点的(x, y)坐标
    color -- 多边形的颜色，默认为红色
    show_axes -- 是否显示包含负坐标的坐标轴，默认为True
    """
    # 创建一个多边形对象
    polygon = Polygon(vertexes, color=color)
   
    # 绘制图形
    fig, ax = plt.subplots()
    ax.add_patch(polygon)
   
    if show_axes:
        # 设置坐标轴界限以包含负坐标
        x_min = min([v[0] for v in vertexes]) - 1
        x_max = max([v[0] for v in vertexes]) + 1
        y_min = min([v[1] for v in vertexes]) - 1
        y_max = max([v[1] for v in vertexes]) + 1
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        plt.axhline(0, color='black',linewidth=0.5)  # 水平线
        plt.axvline(0, color='black',linewidth=0.5)  # 垂直线
        plt.grid(True, linestyle='--', alpha=0.5)  # 显示网格线
        ax.set_aspect('equal')  # 设置坐标轴比例相等
 
    # 显示图形
    plt.show()

def draw_circle(center_x, center_y, radius, color='green', show_axes=True):
    """绘制一个圆，并可选地显示包含负坐标的坐标轴。
   
    参数:
    center_x, center_y -- 圆心的坐标
    radius -- 圆的半径
    color -- 圆的颜色，默认为绿色
    show_axes -- 是否显示包含负坐标的坐标轴，默认为True
    """
    # 创建一个圆对象
    circle = plt.Circle((center_x, center_y), radius, color=color, fill=False)
   
    # 绘制图形
    fig, ax = plt.subplots()
    ax.add_artist(circle)
   
    if show_axes:
        # 设置坐标轴界限以包含负坐标
        ax.set_xlim(center_x - radius - 1, center_x + radius + 1)
        ax.set_ylim(center_y - radius - 1, center_y + radius + 1)
        plt.axhline(0, color='black',linewidth=0.5)  # 水平线
        plt.axvline(0, color='black',linewidth=0.5)  # 垂直线
        plt.grid(True, linestyle='--', alpha=0.5)  # 显示网格线
        ax.set_aspect('equal')  # 设置坐标轴比例相等
 
    # 显示图形
    plt.show()


    