from posixpath import abspath
import re
import shutil
import os

dateRegex = re.compile(r'''
    ^(.*?)
    ([0-1]?[0-9])
    -     
    ([0-3]?[0-9])
    -
    (\d{4})
    (.*?)$
''',re.VERBOSE)

for amerfilename in os.listdir('.'):
    mo = dateRegex.search(amerfilename)
    
    if mo == None:
        continue
    beforeInfo = mo.group(1)
    monthInfo = mo.group(2)
    dayInfo = mo.group(3)
    yearInfo = mo.group(4)
    afterInofo = mo.group(5)

    newfilename = beforeInfo+dayInfo+'-'+monthInfo+'-'+yearInfo+afterInofo

    absofPath = os.path.abspath('.')
    print(absofPath)
    amerpath = os.path.join(absofPath,amerfilename)
    newpath = os.path.join(absofPath,newfilename)

    print('rename "%s" to "%s"...'%(amerpath,newpath))
    # shutil.move(amerpath,newpath)
    