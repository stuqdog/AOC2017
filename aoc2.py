def line_check(line):
    line = [int(x) for x in line.split()]
    return max(line) - min(line)

with open("aoc2.txt") as f:
        print(sum(line_check(line) for line in f))
