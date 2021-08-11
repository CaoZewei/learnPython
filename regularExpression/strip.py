import re
def strip(str,deleteStr = None):
    if None == deleteStr:
        r = re.compile('^\s*|\s*$')
    else:
        r = re.compile('['+deleteStr+']*')

    s = r.sub('',str)
    return s

str ='asfdgfadsgfdfASFSAFDADSF'
print(str)
print(strip(str,'fdFDA'))


