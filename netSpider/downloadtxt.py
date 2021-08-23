import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('there was a problem:%s'%(exc))

with open('RomeoAndJuliet.txt', 'wb+') as playFile:
    for chunk in res.iter_content(100000):
        playFile.write(chunk)

s