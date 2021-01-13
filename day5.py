import math

file = []
with open('day5_input.txt') as my_file:
    for line in my_file:
        file.append(line.rstrip())


def get_row(str):
    start = 0
    stop = 127
    for i in range(0, 7, 1):
        char = str[i]
        length = stop - start
        if char == 'F':
            start = start
            stop = start + int(length / 2)
        elif char == 'B':
            start = start + math.ceil(length / 2)
            stop = stop
    return start


def get_column(str):
    start = 0
    stop = 7
    for i in range(7, 10, 1):
        char = str[i]
        length = stop - start
        if char == 'L':
            start = start
            stop = start + int(length / 2)
        elif char == 'R':
            start = start + math.ceil(length / 2)
            stop = stop
    return start


id_max = 0
ids = []

for line in file:
    row = get_row(line)
    column = get_column(line)
    id = row * 8 + column
    ids.append(id)
    if id > id_max:
        id_max = id

ids.sort()
found = 0

for i in range(1, len(ids), 1):
    # print(ids[i - 1])
    if (ids[i] - ids[i - 1]) != 1:
        found = ids[i] - 1
    # print(id)

print("ID_max: {}".format(id_max))
print("your seat: {}".format(found))
