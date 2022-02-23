import poem
import sys
import pygame

# 初始化加载
poem.loadpoem()
pygame.init()

# 创建窗口
screen = pygame.display.set_mode([400,450])
screen.fill([246,203,144])
pygame.display.flip()

# 主循环
while True:
  p1,p2=poem.form()
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      quit()

