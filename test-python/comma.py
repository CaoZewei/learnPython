def comma(test_list):
    s = test_list[0:-1]
    last_s = 'and '+test_list[-1]
    s.append(last_s)
    str = ','.join(s)
    return str


spam = ['apples', 'bananas', 'tofu', 'cats']
s = comma(spam)
print(s)
