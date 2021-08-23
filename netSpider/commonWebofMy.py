#! python3
# cWeb----commonWebofMy
# commonWebofMy.py - Save and load common web 
# Usage: python.exe commonWebofMy.py save <keyword> <url>- save url to keyword
# python.exe commonWebofMy.py save <keyword> - save clipboard to keyword
# python.exe commonWebofMy.py <keyword> - load keyword and open url
# python.exe commonWebofMy.py list - load all keyword and show it
# python.exe commonWebofMy.py delete all - delete all keywords and urls
# python.exe commonWebofMy.py delete <keyword> - delete target keyword and url

#下一步可以把常用网站用shelve保存起来，用关键字直接打开
import webbrowser,sys,pyperclip,shelve

webShelf = shelve.open('myWeb')
if len(sys.argv) >= 3 and sys.argv[1].lower()=='save':
    if len(sys.argv) == 3:
        url = pyperclip.paste()
        webShelf[sys.argv[2]] = url
    else:
        url = sys.argv[3]
        webShelf[sys.argv[2]]= url
    print('save url:',url,'keyword:',sys.argv[2])
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        for i in list(webShelf.keys()):
            print(i)
    elif sys.argv[1] in webShelf:
        openUrl = webShelf[sys.argv[1]]
        webbrowser.open(openUrl)
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2].lower() == 'all':
        webShelf.clear()
    elif sys.argv[2] in webShelf:
        del webShelf[sys.argv[2]]

webShelf.close()
