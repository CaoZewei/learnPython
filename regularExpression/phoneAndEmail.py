import re
import pyperclip

phoneRegex =re.compile(r'''(
    (\d{3}|\(\d{3}\))?         # ?可选匹配
    (\s|-|\.)?                 # \s 一个空白
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+          # +匹配一次或者多次
    @
    [a-zA-z0-9,-]+
    (\.[a-zA-Z]{2,4})
)''',re.VERBOSE)                #注意不要遗漏re.VERBOSE


text =str(pyperclip.paste())
matchs = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x'+groups[8]
    matchs.append(phoneNum)

for email_g in emailRegex.findall(text):
    matchs.append(email_g[0])

if len(matchs) >0:
    pyperclip.copy('\n'.join(matchs))
    print('\n'.join(matchs))
else:
    print('nothing find')
    
re.compile(r'^\d{1,3}(,\d{3})+$')