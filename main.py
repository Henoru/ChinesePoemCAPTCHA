import random
import time
from Module import poem
import pygame

def drawup(font,pos,typ):
  pygame.draw.rect(screen,(255,255,255),(pos[0],pos[1]+20,103,108))
  if typ==1:
    screen.blit(font,(pos[0],pos[1]))
def insideup(pos,poss):
  return (pos[0]>=poss[0]) and (pos[0]<=poss[0]+103) and (pos[1]>=poss[1]+20) and (pos[1]<=poss[1]+20+108)
def drawdown(font,pos,typ):
  pygame.draw.rect(screen,(255,255,255),(pos[0],pos[1],65,65))
  if typ==1:
    screen.blit(font,(pos[0]+15,pos[1]))
def insidedown(pos,poss):
  return (pos[0]>=poss[0]) and (pos[0]<=poss[0]+65) and (pos[1]>=poss[1]) and (pos[1]<=poss[1]+65)

# 初始化加载
poem.loadpoem()
pygame.init()

# 创建窗口
screen = pygame.display.set_mode([400,490])
screen.fill([246,203,144])
pygame.display.flip()

fontup=pygame.font.Font(r'Font\思源宋体.otf',100)
fontdown=pygame.font.Font(r'Font\思源宋体.otf',40)
fonttip=pygame.font.Font(r'Font\思源宋体.otf',20)
fontans=pygame.font.Font(r'Font\思源宋体.otf',20)
#text=fontup.render('我',True,(0,0,255),(255,255,255))
#screen.blit(text,(0,0))
#pygame.display.flip()
show_answer=False
gap=10
x,y=200-150-gap,10
posup=[[x+i*(100+gap),y+j*(100+gap+5)] for i in range(3) for j in range(3)]
gap=0
width=65
x,y=200-(width*2+width//2),385
posdown=[[x+i*(gap+width),y] for i in range(5)]
postip=[x,y+width+5]
# 主循环
while True:
  p1,p2=poem.form()
  random.shuffle(p2[1])
  while p2[1][4] in p1[1]:
    random.shuffle(p2[1]) 
  texts=[text for text in p1[1]]+[p2[1][i] for i in range(4)]
  random.shuffle(texts)
  fontsup=[fontup.render(text,True,(0,0,0)) for text in texts]
  fontsdown=[fontdown.render(text,True,(0,0,0)) for text in texts]
  tip=fonttip.render(p1[0]["title"]+" "+p1[0]["author"],True,(0,0,0))
  for i in range(9):
    drawup(fontsup[i],posup[i],1)  
  for i in range(5):
    pygame.draw.rect(screen,(255,255,255),(posdown[i][0],posdown[i][1],width,width))
  for i in range(1,5):
    pygame.draw.line(screen,(194,194,194),(posdown[i][0],posdown[i][1]+10),(posdown[i][0],posdown[i][1]-10+width))
  pygame.display.flip()
  if show_answer:
    print(p1[1])
  attemp=5
  while attemp:
    guess=False
    ans=[]
    top=0
    used=[False for i in range(9)]
    while not guess:
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          quit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
          pos=event.pos
          for i in range(9):
            if top<5 and (not used[i]) and insideup(pos,posup[i]):
              ans.append(i)
              used[i]=True
              drawup(fontsup[i],posup[i],0)
              drawdown(fontsdown[i],posdown[top],1)
              if top:
                pygame.draw.line(screen,(194,194,194),(posdown[top][0],posdown[top][1]+10),(posdown[top][0],posdown[top][1]-10+width))
              pygame.display.flip()
              top=top+1
          if top and insidedown(pos,posdown[top-1]):
            top=top-1
            x=ans[top]
            used[x]=False
            ans.pop()
            drawup(fontsup[x],posup[x],1)
            drawdown(fontsdown[x],posdown[top],0)
            if top:
              pygame.draw.line(screen,(194,194,194),(posdown[top][0],posdown[top][1]+10),(posdown[top][0],posdown[top][1]-10+width))
            pygame.display.flip()
        elif event.type==pygame.KEYDOWN:
          if event.key==13:
            show_answer=not show_answer
            if show_answer:
              print(p1[1])
      if top==5:
        guess=True
    answer=[texts[x] for x in ans]
    if answer==p1[1]:
      print(answer)
      attemp=1
    while top:
      top=top-1
      x=ans[top]
      ans.pop()
      drawup(fontsup[x],posup[x],1)
      drawdown(fontsdown[x],posdown[top],0)
      if top:
        pygame.draw.line(screen,(194,194,194),(posdown[top][0],posdown[top][1]+10),(posdown[top][0],posdown[top][1]-10+width))
    if attemp==3:
      screen.blit(tip,(postip[0],postip[1]))
    pygame.display.flip()
    attemp=attemp-1
  screen.fill([246,203,144])
  answer=[p1[0]["title"],p1[0]["author"]]+[text for text in p1[0]["paragraphs"]]
  answerfont=[fontans.render(x,True,(0,0,0)) for x in answer]
  y=30
  for font in answerfont:
    x=200-font.get_size()[0]//2
    screen.blit(font,(x,y))
    y=y+25
  pygame.display.flip()
  click=False
  time.sleep(1)
  while not click:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        quit()
      elif event.type==pygame.MOUSEBUTTONDOWN:
        click=True
      elif event.type==pygame.KEYDOWN:
        if event.key==13:
          show_answer=not show_answer
          if show_answer:
            print(p1[1])
  screen.fill([246,203,144])
  pygame.display.flip()