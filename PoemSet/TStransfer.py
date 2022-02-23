# Tranditional to Simplified
from tkinter.filedialog import Open
from opencc import OpenCC

input=open("PoemSet\poemsetT.json","r",encoding='utf-8')
T=input.read()
S=OpenCC('t2s').convert(T)
output=open("PoemSet\poemsetS.json","w",encoding='utf-8')
output.write(S)
input.close()
output.close()
