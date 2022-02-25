import json
import random
import re

def loadpoem():
  input=open("PoemSet\poemset.json","r",encoding='utf-8')
  global data
  data=json.load(input)
  input.close()
  return
def get5(x):
  list5=[]
  for item in x["paragraphs"]:
    sents=re.split('。|，|！|？',item)
    for sent in sents:
      if len(sent)==5:
        list5.append(sent)
  return list5[random.randrange(len(list5))]
def form():
  a=random.randrange(len(data))
  b=random.randrange(len(data))
  while a==b:
    b=random.randrange(len(data))
  return (data[a],list(get5(data[a]))),(data[b],list(get5(data[b])))
