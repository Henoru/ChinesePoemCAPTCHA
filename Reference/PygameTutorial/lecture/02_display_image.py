"""
Tutorial 02: 显示图片
__author__ = 201220014@smail.nju.edu.cn
"""

import pygame

# 构建最小游戏系统
pygame.init()
window = pygame.display.set_mode((828, 825))
pygame.display.set_caption('显示图片')

# 游戏启动页面的静态效果一般写在此处
# 1. 加载图片
bear_image = pygame.image.load('resource/code_bear.jpeg')

# 2.渲染图片
# blit(渲染对象， 位置信息-坐标)
# 计算机窗口坐标系默认以左上角为坐标原点，所有的对象坐标也默认为左上角坐标
window.blit(bear_image, (0, 0))

# 3. 操作图片(optional)
# 1) 获取图片位置和大小
w, h = bear_image.get_size()  # 获取图片大小(width, height)
x_coordinate, y_coordinate, width, height = bear_image.get_rect()  # 获取图片矩形信息(x, y, width, height)
# 2) 旋转和缩放
# scale(缩放对象， 目标大小) - 不固定比例
new_bear1 = pygame.transform.scale(bear_image, (100, 100))
# rotozoom(缩放/旋转对象， 旋转角度， 缩放比例) zoom + rotate
new_bear2 = pygame.transform.rotozoom(bear_image, 90, 0.5)

# 4. 刷新显示页面
pygame.display.flip()  # 第一次刷新用flip()，第二次以及第二次之后的刷新用update()

while True:
    # 游戏帧的刷新一般写在此处
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
