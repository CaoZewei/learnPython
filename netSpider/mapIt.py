#! python3
#mapit----mapIt
# mapIt.py - Search location in baidu map
# Usage: python.exe mapIt.py <keyword> - search keyword
# python.exe mapIt - Loads keyword from clipboard and search for it.
import webbrowser,sys,pyperclip
import logging

if len(sys.argv)>1:
    #get Location for search 
    location = ''.join(sys.argv[1:])
else:
    location = pyperclip.paste()
url = 'https://map.baidu.com/search/中国/@11575600.246372549,3577144.4050000003,11.46z?querytype=s&da_src=shareurl&wd=中国'
url = url.replace("中国",location)##replace不会改变原来string的内容，需要重新赋值给url
webbrowser.open(url)


#下一步可以把常用网站用shelve保存起来，用关键字直接打开