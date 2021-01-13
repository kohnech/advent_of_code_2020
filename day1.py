import math

#part 1
array = []
with open('day1_input.txt') as my_file:
    for line in my_file:
        array.append(int(line.rstrip()))

numbers = []

for ind in range(len(array)):
    for ind2 in range(ind + 1, len(array), 1):
        if (array[ind] + array[ind2]) == 2020:
            print("found! {a} {b}".format(a=array[ind], b=array[ind2]))
            numbers.append(array[ind])
            numbers.append(array[ind2])

print("answer part1: {}".format(numbers[0] * numbers[1]))
numbers.clear()

#part 2
def part2():
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if (array[i] + array[j] + array[k]) == 2020:
                    print("found! {a} {b} {c}".format(a=array[i], b=array[j], c=array[k]))
                    numbers.append(array[i])
                    numbers.append(array[j])
                    numbers.append(array[k])
                    return

part2()
            
print("answer part2: {}".format(numbers[0] * numbers[1] * numbers[2]))