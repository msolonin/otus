some_file = open("new_write.txt", "a")

text = """Пробелы - самый предпочтительный метод отступов.
Табуляция должна использоваться только для поддержки кода, написанного с отступами с помощью табуляции.
"""

some_file.write(text)

some_file.close()
