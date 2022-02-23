"""
Tutorial 03: 显示文字
__author__ = 201220014@smail.nju.edu.cn
"""

import pygame

pygame.init()
window = pygame.display.set_mode((400, 600))
pygame.display.set_caption('显示图片')
# 设置背景色
window.fill((255, 255, 255))

# 显示文字
# 1. 创建字体对象
# Font(字体文件路径, 字体大小)
font = pygame.font.Font('resource/Alibaba-PuHuiTi-Regular.otf', 30)

# 2. 创建文字对象
# render(文字内容, 是否去锯齿, 文字颜色, 底色)
text = font.render('Hello,熊桑!', True, (0, 0, 255))

# 3. 渲染文字到窗口上
window.blit(text, (0, 0))

# 4. 操作文字对象(optional)
# 1) 获取大小
w, h = text.get_size()
x_coordinate, y_coordinate, width, height = text.get_rect()
# 2) 缩放和旋转
new_text1 = pygame.transform.scale(text, (200, 50))
new_text2 = pygame.transform.rotozoom(text, 90, 2)

# 5. 刷新显示页面
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


