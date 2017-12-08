import re

registers = {}
highest_value = 0

with open('aoc8.txt') as f:
    instructions = [x.strip('\n') for x in f]

def add_value(info):
    if info[2] == "inc":
        registers[info[1]] += int(info[3])
    else:
        registers[info[1]] -= int(info[3])

for instruction in instructions:
    info = re.match("(.+)? (inc|dec) (.*) if (.+)? (.+)? (.*)", instruction, re.I)
    if not info:
        print(instruction)
    if info[1] not in registers:
        registers[info[1]] = 0
    if info[4] not in registers:
        registers[info[4]] = 0
    if info[5] == "==":
        if registers[info[4]] == int(info[6]):
            add_value(info)

    elif info[5] == ">=":
        if registers[info[4]] >= int(info[6]):
            add_value(info)

    elif info[5] == "<=":
        if registers[info[4]] <= int(info[6]):
            add_value(info)

    elif info[5] == "<":
        if registers[info[4]] < int(info[6]):
            add_value(info)

    elif info[5] == ">":
        if registers[info[4]] > int(info[6]):
            add_value(info)

    elif info[5] == "!=":
        if registers[info[4]] != int(info[6]):
            add_value(info)

    if max(registers.values()) > highest_value:
        highest_value = max(registers.values())

print(max(registers.values()))
print(highest_value)
