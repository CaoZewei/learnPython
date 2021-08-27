import requests,sys,webbrowser,bs4

print('baidu...')
url = 'https://xueshu.baidu.com/s?wd='+''.join(sys.argv[1:])
print(url)
res = requests.get(url)
res.raise_for_status
print(type(res))
soup = bs4.BeautifulSoup(res.text,features='lxml')

linkElemes = soup.select('a')
print(len(linkElemes))
# linkopen = min(5,len(linkElemes))

# for i in range(linkopen):
#     print(linkElemes[i])
