instr = {}

with open('aoc13.txt') as f:
    for line in f:
        depth, view = line.strip().split(': ')
        instr[int(depth)] = (list(range(int(view)))
                          + sorted(list(range(1, int(view) - 1)), reverse=True))

print("Part one: {}".format(sum(int(x) * (max(instr[x]) + 1)
     for x in instr if instr[x][x % len(instr[x])] == 0)))

delay = 0
while True:
    if all(instr[x][(x + delay) % len(instr[x])] != 0 for x in instr):
        print("Part two: {}".format(delay))
        break
    delay += 1
