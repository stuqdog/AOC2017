with open("aoc24.txt") as f:
    ports = [sorted(list(map(int, line.strip().split('/')))) for line in f]

print(ports)
# for i, line in enumerate(ports):
#     ports[i] = sorted(line)
# print(ports)

solution1 = 0
solution2 = 0
solution2sum = 0

possible = [[sorted(x)] for x in ports if 0 in x]
print(possible)

while possible:
    continues = False
    for port in ports:
        if port in possible[0] or port[::-1] in possible[0]:
            pass

        elif port[0] == possible[0][-1][1]:
            new = possible[0] + [port]
            possible.append(new)
            continues = True
        elif port[1] == possible[0][-1][1]:
            new = possible[0] + [sorted(port, reverse=True)]
            possible.append(new)
            continues = True
    if not continues:
        total = 0
        for value in possible[0]:
            total += sum(x for x in value)
        if total > solution1:
            solution1 = total
        if len(possible[0]) > solution2:
            solution2 = len(possible[0])
            solution2sum = total
        if len(possible[0]) == solution2:
            solution2sum = max(total, solution2sum)
    del possible[0]

print("Part one:", solution1)
print("Part two:", solution2sum)
