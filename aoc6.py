with open('aoc6.txt') as f:
    for line in f:
        layout = [int(x) for x in line.strip().split()]


previous_positions = {}
moves = 0


while True:
    val = max(layout)
    length = len(layout)

    start = layout.index(val)

    i = 0
    while layout[start] != 0:
        layout[(start + i) % length] += 1
        layout[start] -= 1
        i += 1
    if str(layout) in previous_positions:
        break
    moves += 1
    previous_positions[str(layout)] = moves

print("part 1: {}".format(moves + 1))
print("part two: {}".format(moves + 1 - previous_positions[str(layout)]))
