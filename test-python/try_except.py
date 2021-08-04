# try:
#     for i in range(10):
#         print(5/i)
# except ZeroDivisionError:
#     print('除数不能为0')


# for i in range(10):
#     try:
#         print(5/i)
#     except ZeroDivisionError:
#         print('除数不能为0')


try:
    with open('test.txt') as file:
        contents = file.read()
    print(contents.strip())
except FileNotFoundError:
    print('no file')
