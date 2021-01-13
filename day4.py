import json
import re


class Passport:
    def __init__(self):
        self.myvars = {}

    def is_valid(self):
        # if all (k in self.myvars for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        #     return True
        # return False
        if 'byr' not in self.myvars:
            return False
        if 'iyr' not in self.myvars:
            return False
        if 'eyr' not in self.myvars:
            return False
        if 'hgt' not in self.myvars:
            return False
        if 'hcl' not in self.myvars:
            return False
        if 'ecl' not in self.myvars:
            return False
        if 'pid' not in self.myvars:
            return False
        if not self.check_byr(self.myvars['byr']):
            return False
        if not self.check_iyr(self.myvars['iyr']):
            return False
        if not self.check_eyr(self.myvars['eyr']):
            return False
        if not self.check_hgt(self.myvars['hgt']):
            return False
        if not self.check_hcl(self.myvars['hcl']):
            return False
        if not self.check_ecl(self.myvars['ecl']):
            return False
        if not self.check_pid(self.myvars['pid']):
            return False
        return True

    def check_byr(self, str):
        byr = int(str)
        if len(str) == 4 and byr >= 1920 and byr <= 2002:
            return True
        return False

    def check_iyr(self, str):
        iyr = int(str)
        if len(str) == 4 and iyr >= 2010 and iyr <= 2020:
            return True
        return False

    def check_eyr(self, str):
        eyr = int(str)
        if len(str) == 4 and eyr >= 2020 and eyr <= 2030:
            return True
        return False

    def check_hgt(self, str):
        unit = str[len(str) - 2:]
        value = int(str[:len(str) - 2])
        print("unit: {} value: {}".format(unit, value))
        if unit == "cm" and value >= 150 and value <= 193:
            return True
        if unit == "in" and value >= 59 and value <= 76:
            return True
        return False

    def check_hcl(self, str):
        if re.search(r'^#(?:[0-9a-f]{3}){1,2}$', str):
            return True
        return False

    def check_ecl(self, str):
        colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        for colour in colours:
            if colour in str:
                return True
        return False

    def check_pid(self, str):
        if len(str) == 9:
            return True
        return False

    def print_passport(self):
        print(self.myvars)

    def append_data(self, data):
        name, var = data.partition(":")[::2]
        # print("(name) {} : (var) {}".format(name, var))
        self.myvars[name.strip()] = var.strip()

    def readline(self, line):
        lines = line.split()
        for newline in lines:
            self.append_data(newline)


passports = []

with open('day4_input.txt') as my_file:
    p = Passport()
    for line in my_file:
        if not line.strip():
            passports.append(p)
            p = Passport()
        else:
            p.readline(line.rstrip())
    # append last passport
    passports.append(p)


valid = 0
for passport in passports:
    if passport.is_valid():
        passport.print_passport()
        valid = valid + 1


print("Number of valid passports: {}".format(valid))


# p1 = Passport()
# p1.print()

# p.check_hgt("170cm")
# print(p.check_ecl("aaa"))

print(p.check_hgt("60in"))
