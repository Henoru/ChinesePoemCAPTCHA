"""
Tutorial 06: 动画控制(含键盘事件)
__author__ = 201220014@smail.nju.edu.cn
"""

import pygame

WIN_WIDTH, WIN_HEIGHT = 1200, 900
WHITE = (255, 255, 255)

# 初始化游戏和窗口
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('动画控制')
window.fill(WHITE)

# 导入帧图片
frames = []
for i in range(7):
    image_path = 'resource/animation_demo/frame_{}.tiff'.format(i + 1)
    frame = pygame.image.load(image_path)
    frames.append(frame)

# 初始化图片信息
frame_index = 0  # 图片帧序号
x_coordinate, y_coordinate = 100, 100  # 初始位置
x_vel, y_vel = 0, 0  # 初始速度
window.blit(frames[frame_index], (x_coordinate, y_coordinate))
pygame.display.flip()

frame_counter = 0  # 帧计数器，记录当前是第几帧
SPEED_FACTOR = 5  # 速度因子，当帧数是其倍数时跟新图片帧，用以调整速度

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()  # 获取按键信息

            # 根据键盘的上下左右键移调整速度
            if keys[pygame.K_UP]:
                y_vel = -10
            elif keys[pygame.K_DOWN]:
                y_vel = 10
            elif keys[pygame.K_LEFT]:
                x_vel = -10
            elif keys[pygame.K_RIGHT]:
                x_vel = 10
        else:
            x_vel, y_vel = 0, 0

    # 更新帧计数器
    frame_counter = (frame_counter + 1) % SPEED_FACTOR  # 模运算是为了防止程序长时间运行导致数据过大，内存越界

    if frame_counter == 0:
        frame_index = (frame_index + 1) % 7  # 更新帧

    # 更新位置
    x_coordinate += x_vel
    y_coordinate += y_vel

    # 防止移出屏幕
    if x_coordinate < 0:
        x_coordinate = 0
    if x_coordinate > WIN_WIDTH - frames[frame_index].get_width():
        x_coordinate = WIN_WIDTH - frames[frame_index].get_width()
    if y_coordinate < 0:
        y_coordinate = 0
    if y_coordinate > WIN_HEIGHT - frames[frame_index].get_height():
        y_coordinate = WIN_HEIGHT - frames[frame_index].get_height()

    # 更新窗口
    window.fill(WHITE)
    window.blit(frames[frame_index], (x_coordinate, y_coordinate))
    pygame.display.update()




