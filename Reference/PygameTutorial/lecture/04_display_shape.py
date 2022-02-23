"""
Tutorial 04: 显示图形
__author__ = 201220014@smail.nju.edu.cn
"""

import pygame
from math import pi


pygame.init()
window = pygame.display.set_mode((400, 600))
pygame.display.set_caption('显示图形')
window.fill((255, 255, 255))

# 显示图形
# 1. 画直线
# line(绘图设备, 颜色, 起点, 终点, 线宽=1)
pygame.draw.line(window, (255, 0, 0), (10, 20), (200, 20))

# 2. 画折线
# lines(绘图设备, 颜色, 是否闭合, 点的序列, 线宽=1)
points = [(10, 300), (100, 160), (180, 260), (300, 100)]
pygame.draw.lines(window, (0, 255, 0), True, points, 3)

# 3. 画圆
# circle(绘图设备, 颜色, 圆心坐标, 半径, 线宽=0)
pygame.draw.circle(window, (0, 0, 255), (200, 250), 100, 2)  # 线宽为0表示填充

# 4. 画矩形
# rect(绘图设备, 颜色, 矩形范围, 线宽=0)
# 矩形范围是一个4元组: (x, y, width, height)
pygame.draw.rect(window, (0, 0, 0), (100, 70, 100, 200))  # 线宽为0表示填充

# 5. 画椭圆
# ellipse(绘图设备, 颜色, 矩形范围, 线宽=0)
# 椭圆的标准外切矩形和椭圆唯一对应，故而可以使用矩形范围来限定椭圆的形状与位置
pygame.draw.ellipse(window, (225, 0, 225), (100, 70, 100, 200), 2)

# 6.画弧线
# draw(绘图设备, 线的颜色, 矩形范围, 起始弧度, 终止弧度, 线宽=1)
# pygame支持绘制的弧线是椭圆的一部分，起始弧度和终止弧度的范围是0 ~ 2 * pi
# 矩形位置坐标系遵循窗口坐标系，弧度坐标系遵循数学坐标系
pygame.draw.arc(window, (0, 225, 225), (100, 70, 100, 200), 0, pi, 10)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
