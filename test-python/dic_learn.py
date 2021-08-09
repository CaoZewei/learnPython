dict_test = {'Name': 'Runoob', 'num': {'first_num': '66', 'second_num': '70'}, 'age': '15'}

a = dict_test.get('num', 0)
print(a)
b = a.get("first_num", 0)
print(b)
print(dict_test.get('first_num', -1))
dict_test['birth'] = 20210914
dict_test['birth'] += 1
print(dict_test)
