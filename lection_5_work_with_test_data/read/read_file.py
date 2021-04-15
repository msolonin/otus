file = open('../data/data.txt', 'rb')
# file = open('../data/1.jpg', 'rb')

# чтение всего файла
print(file.read())

# количество символов
# print(file.read(20))

# построчно
# print(file.readline())
# print(file.readline())
# print(file.read())

# список
# lines = file.readlines()
# print(file.readlines())

# построчно
# for item in file:
#     item = item.strip()
#     print(item)

file.close()
