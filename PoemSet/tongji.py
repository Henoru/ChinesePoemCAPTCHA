import json

A=open("PoemSet\poemsetS.json","r",encoding='utf-8')
B=open("PoemSet\poemset.json","r",encoding='utf-8')

dataA=json.load(A)
dataB=json.load(B)
print(len(dataA))
print(len(dataB))
A.close()
B.close()