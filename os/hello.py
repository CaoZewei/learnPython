import os
path = os.getcwd() ##获取当前工作目录的绝对文件路径
textpath = path+"\hello.txt"
with open(textpath,'r') as file :
    print(file.read())

sonnetpath = path+'\sonnet29.txt'
with open(sonnetpath,'r') as sonnetFile:
    lines = sonnetFile.readlines()
    print(lines)
    for line in lines:
        print(line,end="")


baconPath = 'bacon.txt'
with open(baconPath,'w') as baconFile:##w 擦除写入
    baconFile.write('hello os write!!\n')

with open(baconPath,'a') as baconFile:##a 是附加写入
    baconFile.write('bacon is very delicious')

