

# read input file
file = []
with open('day2_input.txt') as my_file:
    for line in my_file:
        file.append(line.rstrip())

def check_in_interval(password, letter, minimum, maximum):
    count = password.count(letter)
    if count >= minimum and count <= maximum:
        return True
    return False

# part2
def check_if_position(password, letter, pos1, pos2):
    if password[pos1 - 1] == letter and password[pos2 - 1] != letter:
        return True
    elif password[pos1 - 1] != letter and password[pos2 - 1] == letter:
        return True
    return False

def split_line(line):
    arr = line.split(':')
    password = arr[1].strip()
    arr2 = arr[0].strip().split(" ")
    arr3 = arr2[0].split("-")
    letter = arr2[1]
    min_ = int(arr3[0])
    max_ = int(arr3[1])
    return (password, letter, min_, max_)

valid_passwords = 0

for line in file:
    # line = "6-8 s: svsssszslpsp"
    passw, letter, minimum, maximum = split_line(line)
    if check_if_position(passw, letter, minimum, maximum):
        valid_passwords = valid_passwords + 1

print("valid passpords: {}".format(valid_passwords))
    
