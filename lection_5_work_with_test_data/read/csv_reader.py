import csv
from csv import DictReader

with open('../data/data.csv', 'r') as file:
    reader = csv.reader(file)

    header = next(reader)
    # print(header)
    # data = []
    for item in reader:
        # print(item)
        # print(dict(zip(header, item)))
        # data.append(dict(zip(header, item)))
        print(dict(zip(header, item))['first_name'])  # Get any key from dict by key name
    # print(data)


# with open('../data/data.csv') as f:
#     reader = DictReader(f)
#
#     # Итерируемся по данным делая из них словари
#     for row in reader:
#         print(row)
#         print(row['first_name'])
