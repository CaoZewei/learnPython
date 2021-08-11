import re
# r =re.compile(r'[A-Z][a-z]*\sNakamoto')

# s = 'my name is Mr Nakamoto'

# m = r.search(s)
# print(m)


r = re.compile(r'(^Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).',re.IGNORECASE)

s =  'ALICE THROWS FOOTBALLS.'
m = r.search(s)
print(m)