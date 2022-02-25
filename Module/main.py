import random
import time
from turtle import width
import poem
import pygame

def drawup(font,pos):
  pygame.draw.rect(screen,(255,255,255),(pos[0],pos[1]+20,103,108))
  screen.blit(font,(pos[0],pos[1]))
# 初始化加载
poem.loadpoem()
pygame.init()

# 创建窗口
screen = pygame.display.set_mode([400,470])
screen.fill([246,203,144])
pygame.display.flip()

fontup=pygame.font.Font(r'Font\思源宋体.otf',100)
fontdown=pygame.font.Font(r'Font\思源宋体.otf',50)
#text=fontup.render('我',True,(0,0,255),(255,255,255))
#screen.blit(text,(0,0))
#pygame.display.flip()
gap=10
x,y=200-150-gap,10
posup=[[x+i*(100+gap),y+j*(100+gap+5)] for i in range(3) for j in range(3)]
gap=0
width=65
x,y=200-(width*2+width//2),385
posdown=[[x+i*(gap+width),y] for i in range(5)]
# 主循环
while True:
  p1,p2=poem.form()
  random.shuffle(p2[1])
  while p2[1][4] in p1[1]:
    random.shuffle(p2[1]) 
  texts=[text for text in p1[1]]+[p2[1][i] for i in range(4)]
  random.shuffle(texts)
  fonts=[fontup.render(text,True,(0,0,0)) for text in texts]
  for i in range(9):
    drawup(fonts[i],posup[i])  
  #[print(x.get_size()) for x in fonts]
  for i in range(5):
    pygame.draw.rect(screen,(255,255,255),(posdown[i][0],posdown[i][1],width,width))
  pygame.display.flip()
  print(p1[1])
  time.sleep(1)
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      quit()


