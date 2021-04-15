# Context manager https://pythonworld.ru/osnovy/with-as-menedzhery-konteksta.html
#__enter__, __exit__ magic methoda

# with open('../data/data.txt', 'r') as file:
#     item = file.read()
#
# print(item)

with open('../data/data.txt', 'r') as file:
    for item in file.readlines():
        print(item)
