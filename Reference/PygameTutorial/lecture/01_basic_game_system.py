"""
Tutorial 01: pygame的最小游戏系统，一个最基本的框架
__author__ = 201220014@smail.nju.edu.cn
"""

import pygame


# 1. 初始化操作，主要是对于硬件(鼠标、键盘、声音、显示器)进行一些初始化操作
pygame.init()

# 2. 创建游戏窗口
# set_mode(size=(width,height))
window = pygame.display.set_mode((400, 600))
# 设置游戏标题
pygame.display.set_caption('最小游戏系统')
# 设置背景颜色
window.fill((255, 255, 255))  # 三元组为RGB颜色格式(Red, Green, Bue), 这里是白色
pygame.display.flip()  # 初始刷新界面

# 3. 创建主循环(游戏循环：game loop)，让游戏保持一直运行的状态
# 在游戏循环中需要监测事件
while True:
    # 4. 检测事件
    for event in pygame.event.get():  # get()函数有可能获取多个事件，需要循环遍历
        # 检测事件类型并处理
        if event.type == pygame.QUIT:  # 如果关闭按钮被点击
            quit()


