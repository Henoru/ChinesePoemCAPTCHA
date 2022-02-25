import random

from scipy import rand
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

fontup=pygame.font.Font(r'Font\思源宋体.otf',100)
fontdown=pygame.font.Font(r'Font\思源宋体.otf',50)
#text=fontup.render('我',True,(0,0,255),(255,255,255))
#screen.blit(text,(0,0))
#pygame.display.flip()
gap=5
x,y=200-150-gap,32
posup=[[x+i*(100+gap),y+j*(100+gap)] for i in range(3) for j in range(3)]
gap=10
x,y=200-125-2*gap,362
posdown=[[x+i*(gap+50),y] for i in range(5)]
# 主循环
while True:
  p1,p2=poem.form()
  random.shuffle(p2[1])
  while p2[1][4] in p1[1]:
    random.shuffle(p2[1]) 
  texts=[text for text in p1[1]]+[p2[1][i] for i in range(4)]
  fonts=[fontup.render(text,True,(0,0,0),(255,255,255)) for text in texts]
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      quit()


