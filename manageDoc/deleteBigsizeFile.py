import os,shutil

#遍历目录树
path='D:\\Study\\python'
os.chdir(path)

#1MB=?bit,os.path.getsize返回的是字节
delete_size=1024

def findFolder(path):
    
    for folderName, subfolders, filenames in os.walk(path):         
        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.txt'):
                if os.path.getsize(os.path.join(folderName,filename))>=1024:
                    print(os.path.join(folderName,filename))
