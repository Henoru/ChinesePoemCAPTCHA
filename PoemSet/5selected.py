import json
import re
def is_five(items):
  for item in items:
    sents=re.split('。|，|！|？',item)
    for sent in sents:
      if len(sent)==5:
        return True
  return False
input=open("PoemSet\poemsetS.json","r",encoding='utf-8')
data=json.load(input)
upd=[]
for poem in data:
  if is_five(poem["paragraphs"]):
    upd.append(poem)
output=open("PoemSet\poemset.json","w",encoding='utf-8')
json.dump(upd,output,ensure_ascii=False)
input.close()
output.close()