import os
path = os.getcwd()
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
with open(baconPath,'w') as baconFile:
    baconFile.write('hello os write!!\n')

with open(baconPath,'a') as baconFile:
    baconFile.write('bacon is very delicious')

