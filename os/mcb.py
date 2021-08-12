import shelve,pyperclip,sys

mcbShelf =shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
    mcbShelf[sys.argv[2]]==pyperclip.paste()
elif len(sys.argv) == 2:
    pass

mcbShelf.close()