"""
Tutorial 05: 动画原理
__author__ = 201220014@smail.nju.edu.cn
"""

import pygame

# 窗口宽高，设置全局变量，避免硬编码，方便后期调整
WIN_WIDTH, WID_HEIGHT = 400, 600

# 初始化操作
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WID_HEIGHT))
pygame.display.set_caption('动画原理')
window.fill((255, 255, 255))
pygame.display.flip()

# 动画原理(帧动画): 帧的快速切换 + 视觉暂留效应
# 示例: 变化的球, 包括: 移动、缩放、颜色变化

# 显示静态球(熊桑偷个懒，用圆代表球)
y_coordinate = 100  # 因为向下移动y坐标需要移动，所以不能硬编码 -- 移动动画
radius = 25  # 放大图形需要增加半径值 -- 缩放动画
green_channel = 0  # 修改绿色通道的值可以实现 -- 颜色变化
pygame.draw.circle(window, (255, green_channel, 0), (100, y_coordinate), radius)
pygame.display.update()

while True:
    # 检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    if y_coordinate < WID_HEIGHT - 100:  # 控制动画终止
        y_coordinate += 1  # 移动
        radius += 0.2
        green_channel = (green_channel + 1) % 256  # 颜色通道取值范围是 0～255
        window.fill((255, 255, 255))  # 覆盖之前的圆
        pygame.draw.circle(window, (255, green_channel, 0), (100, y_coordinate), radius)  # 绘制新的圆
        pygame.display.update()







