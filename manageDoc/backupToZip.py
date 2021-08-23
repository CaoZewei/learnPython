import zipfile,os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    filename = os.listdir(folder)
    print(filename)

    number =1
    while True:
        afile = os.path.basename(folder)+'_'+str(number)+'.zip'
        print(afile)
        if afile in filename:
            number+=1
            continue
        else:
            break
    afile = folder+ "\\" +afile
    backupZip = zipfile.ZipFile(afile,'w')
    for foldername,subfoldername,file in os.walk(folder):#浏览目录树
        foldername=os.path.basename(foldername)
        for newfile in file:
            # if newfile.endswith('.zip'):
            if '.zip' in newfile:
                break
            backupZip.write('../'+foldername)
            backupZip.write(os.path.join('../'+foldername,newfile))
            print(os.path.join(foldername,newfile))

# backupToZip('E:\C#code\python\learnPython\manageDoc')


        