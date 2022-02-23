"""
Tutorial 07: 键盘事件
__author__ = 20120014@smail.nju.edu.cn
"""

import pygame

WIN_WIDTH, WIN_HEIGHT = 400, 600
WHITE = (255, 255, 255)

# 初始化游戏和窗口
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('键盘事件')
window.fill(WHITE)
pygame.display.flip()

# 键盘按下、抬起的计数器
down_counter, up_counter = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            # 处理键盘按下事件
            down_counter += 1  # 更新键盘按下计数器
            key_value = event.key  # 获取按键的ASCII编码值
            print('这是第', down_counter, '次键盘按下，按下的键ASCII码是', event.key)  # 打印按键信息
        elif event.type == pygame.KEYUP:
            # 处理键盘抬起事件
            up_counter += 1  # 更新键盘抬起计数器
            key_value = event.key  # 获取按键的ASCII编码值
            print('这是第', up_counter, '次键盘抬起，抬起的键ASCII是', event.key)  # 打印按键信息
