import re
r = re.compile(r'^\d{1,3}(,\d{3})*$')

s = '11'

m = r.search(s)
print(m)