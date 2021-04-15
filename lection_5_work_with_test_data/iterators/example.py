# https://devpractice.ru/python-lesson-15-iterators-and-generators/

import sys

lst = ['test1', 'test2', 'test100500']
lst_size = sys.getsizeof(lst)
# for i in lst:
#     print(i)

it_obj = iter(lst)
it_size = sys.getsizeof(it_obj)
print(it_obj)

print(next(it_obj))
print(next(it_obj))
print(next(it_obj))
print(next(it_obj))
# print(next(it_obj))
# print(next(it_obj))

