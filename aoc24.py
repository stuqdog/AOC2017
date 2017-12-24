with open("aoc24.txt") as f:
    ports = [map(int, line.strip().split('/')) for line in f]

for i, line in enumerate(ports):
    ports[i] = sorted(line)

solution1 = 0
solution2 = 0
solution2sum = 0

ports = sorted(ports, key=lambda x: x[0])
possible = [[x] for x in ports if 0 in x]

while possible:
    continues = False
    for port in ports:
        if port[:] in possible[0] or port[::-1] in possible[0]:
            pass

        elif port[0] == possible[0][-1][1]:
            new = possible[0][:] + [port]
            possible.append(new)
            continues = True
        elif port[1] == possible[0][-1][1]:
            new = possible[0][:] + [sorted(port, reverse=True)]
            possible.append(new)
            continues = True
    if not continues:
        total = 0
        for value in possible[0]:
            total += sum(x for x in value)
        if total > solution1:
            print(total, solution2)
            solution1 = total
        if len(possible[0]) > solution2:
            solution2 = len(possible[0])
            solution2sum = total
        if len(possible[0]) == solution2:
            solution2sum = max(total, solution2sum)
    del possible[0]

print(solution1)
print(solution2sum)
