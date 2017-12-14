instructions = []
solution = 0
grid = []

for x in range(128):
    new = [ord(c) for c in ('flqrgnkx-' + str(x))] + [17,31,73,47,23]
    instructions.append(new)

for row in range(128):
    order = list(range(256))
    skip_size = 0
    point = 0
    short_hash = [0] * 16

    for rounds in range(64):
        for x in instructions[row]:
            for y in range(x // 2):
                order[(point + y) % 256], order[(point + x - y - 1) % 256] = (
                order[(point + x - y - 1) % 256], order[(point + y) % 256])
            point += (skip_size + x)
            skip_size += 1

    for x in range(16):
        for y in range(16):
            short_hash[x] ^= order[x * 16 + y]
    new = ''.join([hex(x)[2:] if len(hex(x)) ==
                   4 else '0' + hex(x)[2:] for x in short_hash])
    data = ''
    for c in new:
        adder = bin(int(c, 16))[2:].zfill(4)
        data += adder
    solution += sum(1 for c in data if c == '1')
    grid.append([c for c in data])

print("Part one: {}".format(solution))


previously_visited = {}
check = [(1, 0), (-1, 0), (0, 1), (0, -1)]
group_num = 0

for x in range(128):
    for y in range(128):
        if grid[x][y] == '1' and (x, y) not in previously_visited:
            previously_visited[(x, y)] = group_num
            to_check = [(x+a[0], y+a[1]) for a in check]
            while to_check:
                new_x, new_y = to_check[0][0], to_check[0][1]
                if new_x in range(128) and new_y in range(128) and (
                            (new_x, new_y) not in previously_visited and
                            grid[new_x][new_y] == '1'):
                    new = [(new_x+a[0], new_y+a[1]) for a in check]
                    previously_visited[(new_x, new_y)] = group_num
                    to_check += new
                del to_check[0]
            group_num += 1

print("Part two: {}".format(group_num))
