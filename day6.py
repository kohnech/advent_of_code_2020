from collections import defaultdict

file = []
with open('day6_input.txt') as my_file:
    for line in my_file:
        file.append(line.rstrip())


def get_yes(groups):
    answers = defaultdict(int)
    # answers = {}
    for person in groups:
        for i in range(len(person)):
            answers[person[i]] += 1
    # print(answers)
    return len(answers.keys())


def get_everyone_yes(groups):
    answers = defaultdict(int)
    # answers = {}
    for person in groups:
        for i in range(len(person)):
            answers[person[i]] += 1
    # print(answers)
    temp = 0
    for key in answers:
        temp = temp + int(answers[key] / len(groups))
    return temp


num_yes = 0
groups = []

for line in file:
    if line == "":
        num_yes = num_yes + get_everyone_yes(groups)
        groups.clear()
        continue
    groups.append(line)


print("yes: {}".format(num_yes))
