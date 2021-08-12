import shelve

shelFile = shelve.open('mydata')
#写入变量
# cats = ['zophie','pooka','Simon']
# shelFile['cats'] = cats

print(type(shelFile))
k =list(shelFile.keys())
v = list(shelFile.values())
print(k,v[0][0])
shelFile.close()