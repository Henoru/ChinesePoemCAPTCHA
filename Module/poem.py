import json
import random

def loadpoem():
  intput=open("PoemSet\poemset.json","w",encoding='utf-8')
  global data
  data=json.load(input)
  input.close()
  return

def form():
  a=random.randrange(len(data))
  b=random.randrange(len(data))
  while a==b:
    b=random.randrange(len(data))
  return data[a],data[b]
