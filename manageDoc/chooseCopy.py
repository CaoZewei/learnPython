import os,shutil

#遍历目录树
path='D:\\Study\\python\\testfiledir'
os.chdir(path)

try:
    os.mkdir('copy_to_this_dir')
except FileExistsError:
    pass

for folderName, subfolders, filenames in os.walk('.'):  
    for filename in filenames:
        if filename.endswith('.txt') or filename.endswith('.pdf'):
            if filename not in os.listdir('copy_to_this_dir'):
                shutil.copy(os.path.join(folderName,filename),'copy_to_this_dir') 
