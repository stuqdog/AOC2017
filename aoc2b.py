def find_value(line):
    line = sorted([int(x) for x in line.split()], reverse = True)
    for i, x in enumerate(line):
        for divisor_index in range(i + 1, len(line)):
            if x % line[divisor_index] == 0:
                return x / line[divisor_index]

with open('aoc2.txt') as f:
    print(sum(find_value(line) for line in f))
