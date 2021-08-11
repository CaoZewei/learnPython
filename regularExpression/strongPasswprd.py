import re

def passwordCheck(str):
    if len(str)>= 8:
        psdRegex1 = re.compile(r'[A-Z]')
        psdRegex2 = re.compile(r'[a-z]')
        psdRegex3 = re.compile(r'[0-9]')
        if psdRegex1.search(str) == None:
            print("你的密码中没有大写字符！")
        elif psdRegex2.search(str) == None:
            print("你的密码中没有小写字符！")
        elif psdRegex3.search(str) ==None:
            print("你的密码中没有数字")
        else:
            print("设置强口令成功！")
    else:
        print('密码太短')




passwordCheck('AfasdfAfasf')