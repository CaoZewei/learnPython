#! python3
#mcb----multiclipboard
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve,pyperclip,sys

mcbShelf =shelve.open('mcb')
print('start')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2].lower() == 'all':
        mcbShelf.clear()#删除所有复制内容
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]#删除对应值
print('end')
mcbShelf.close()

#可以写bat脚本，然后将脚本目录放到环境变量中，这样可以直接在cmd中使用前缀名执行，该文件为：mcb
#运营目录在哪，shelve的临时文件 .bak,.dat,.dir 就会保存在哪里

