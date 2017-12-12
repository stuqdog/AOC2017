import re

with open("aoc12.txt") as f:
    instructions = [line.strip() for line in f]

direct_connections = {}
total_groups = 0

for line in instructions:
    start, connect = re.match("(\d*) <-> (.*)", line).groups()
    direct_connections[int(start)] = [int(x) for x in connect.strip().split(', ')]

while direct_connections:
    connected_to_root = sorted(direct_connections[min(direct_connections.keys())])
    solution = {}

    while connected_to_root:
        for x in direct_connections[connected_to_root[0]]:
            if x not in solution:
                solution[x] = 1
                if x not in connected_to_root:
                    connected_to_root.append(x)
        del connected_to_root[0]
    for y in solution:
        del direct_connections[y]
    groups += 1
    if groups == 1:
        print("Part one: {}".format(len(solution)))

print("Part two: {}".format(groups))
