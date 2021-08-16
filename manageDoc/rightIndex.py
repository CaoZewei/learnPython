import os,re,shutil

path='D:\\Study\\python\\testfiledir'
os.chdir(path)
folder_format=re.compile(r'^spam(.*?)\.txt$')

# 找到指定文件夹中所有带指定前缀的文件
def find_file_name(folder,folder_format):
    #所有符合标准的文件
    originTextFile=[]
    #编号
    num_list=[]
    
    # 查找并提取原始文件名列表，获取文件编号 
    for filename in os.listdir(folder):
            mo=folder_format.search(filename)
            if mo!=None:
                originTextFile.append(filename)              
                num_list.append(mo.group(1))       
    #建立编号序列
    totalNum=[]
    for index in range(1,len(originTextFile)+1):
        totalNum.append('%03d'%index)
    
    #修改文件名，以消除缺失的编号
    for i,v in zip(num_list,totalNum):
        shutil.move('spam%s.txt'%i,'spam%s.txt'%v)
    
find_file_name(path,folder_format)