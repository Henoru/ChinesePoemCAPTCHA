"""
Tutorial 07: 鼠标事件
__author__ = 20120014@smail.nju.edu.cn
"""

import pygame

WIN_WIDTH, WIN_HEIGHT = 400, 600
WHITE = (255, 255, 255)

# 初始化游戏和窗口
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('鼠标事件')
window.fill(WHITE)
pygame.display.flip()

# 鼠标按下、抬起、移动的计数器
down_counter, up_counter, motion_counter = 0, 0, 0
event_counter = 0  # 所有事件计数器

while True:
    # 检测事件
    for event in pygame.event.get():
        # for循环中的代码只有事件发生之后才会执行
        event_counter += 1
        print('这是第', event_counter, '次 **事件**')
        # event的type属性是用来区分不同类型的事件的
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # MOUSEBUTTONDOWN 鼠标按下
            # 处理鼠标按下事件
            down_counter += 1  # 更新计数器
            position = event.pos  # 获取鼠标位置 (x_coordinate, y_coordinate)
            print('这是第', down_counter, '次 **鼠标按下** 在点', position)  # 打印事件信息
        elif event.type == pygame.MOUSEBUTTONUP:  # MOUSEBUTTONUP 鼠标抬起
            # 处理鼠标抬起事件
            up_counter += 1
            position = event.pos
            print('这是第', up_counter, '次 **鼠标抬起** 在点', position)
        elif event.type == pygame.MOUSEMOTION:  # MOUSEMOTION 鼠标移动
            # 处理鼠标移动事件
            motion_counter += 1
            position = event.pos
            print('这是第', motion_counter, '次 **鼠标移动** 在点', position)

