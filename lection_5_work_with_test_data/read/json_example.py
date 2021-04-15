from json import loads, dumps

with open('../data/data.json', 'r') as file:
    j = file.read()
    n = loads(j)
    print(n)
    print(type(n))
    str_js = dumps(n)
    print(str_js)
    print(type(str_js))

