import time
a = time.time()
print(a)
b = time.localtime(a)
print(b)
c = time.asctime(b)
print(c)
d = time.strftime("%H:%M:%S", time.localtime())
print(d)
