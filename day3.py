
array = []
num_of_lines = 0

with open('day3_input.txt') as my_file:
    for line in my_file:
        num_of_lines = num_of_lines + 1
        array.append(list(line.rstrip()))


# 3, 1
num_trees_1 = 0
x = 0

for y in range(num_of_lines):
    if array[y][x] == "#":
        num_trees_1 = num_trees_1 + 1
    x = (x + 3) % len(array[0])


print("Number of trees: {}".format(num_trees_1))

# 1, 1
num_trees_2 = 0
x = 0
for y in range(num_of_lines):
    if array[y][x] == "#":
        num_trees_2 = num_trees_2 + 1
    # y = y + 1
    x = (x + 1) % len(array[0])

print("Number of trees: {}".format(num_trees_2))


# 5, 1
num_trees_3 = 0
x = 0
for y in range(num_of_lines):
    if array[y][x] == "#":
        num_trees_3 = num_trees_3 + 1
    # y = y + 1
    x = (x + 5) % len(array[0])

print("Number of trees: {}".format(num_trees_3))


# 7, 1
num_trees_4 = 0
x = 0
for y in range(num_of_lines):
    if array[y][x] == "#":
        num_trees_4 = num_trees_4 + 1
    # y = y + 1
    x = (x + 7) % len(array[0])

print("Number of trees: {}".format(num_trees_4))


# 1, 2
num_trees_5 = 0
x = 0
for y in range(0, num_of_lines, 2):
    if array[y][x] == "#":
        num_trees_5 = num_trees_5 + 1
    # y = y + 2
    x = (x + 1) % len(array[0])

print("Number of trees: {}".format(num_trees_5))

print("Part 2: {}".format(num_trees_1 * num_trees_2 * num_trees_3 * num_trees_4 * num_trees_5))