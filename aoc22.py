puzzle = '''#.###...#..#..#...##.####
##.##.#..##.#..#.#..#####
.####..###.#.#####.#.##.#
##..#.##.#.#.#...#..##..#
..#...####.#.###.###...#.
#..###.##.###.....#....#.
.#..#.##.##....##...####.
###.##....#...#.##....##.
..#.###..######.#.####...
.#.###..#.##.#..##.######
###.####.#####.####....#.
#...####.#.##...##..#.#..
##.######.#....##.#.####.
.#.#..#...##....#....#...
.####.##.#..##...#..####.
.#.####.##..###..###..##.
...#...####...#.#.#.###.#
#.##.####.#..##.###.####.
.#.#...####....##..####.#
##.###.##..####..#.######
#.#...#.#.##.####........
.......#..##..#.#..###...
.#..###.###........##.#..
.######.......#.#.##.#.#.
.##..#.###.....##.#.#...#'''.strip().split()



for i, line in enumerate(puzzle):
    puzzle[i] = [c for c in line.strip()]

max_x = len(puzzle[0])
max_y = len(puzzle)
x = max_x // 2
y = max_y // 2
solution = 0
direction = 0
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# for part_one in range(10000):
#     if puzzle[y][x] == '#':
#         direction += 1
#         puzzle[y][x] = '.'
#     else:
#         puzzle[y][x] = '#'
#         direction -= 1
#         solution += 1
#
#     x += move[direction % 4][1]
#     y += move[direction % 4][0]
#     if x >= max_x:
#         max_x += 1
#         for line in puzzle:
#             line.append('.')
#     if y >= max_y:
#         new_line = ['.'] * max_x
#         puzzle.append(new_line)
#         max_y += 1
#     if x < 0:
#         for line in puzzle:
#             line.insert(0, '.')
#             x = 0
#             max_x += 1
#     if y < 0:
#         new_line = ['.'] * max_x
#         puzzle.insert(0, new_line)
#         y = 0
#         max_y += 1
# print(solution)


for part_two in range(10000000):
    if puzzle[y][x] == '#':
        direction += 1
        puzzle[y][x] = 'F'
    elif puzzle[y][x] == 'F':
        puzzle[y][x] = '.'
        direction -= 2
    elif puzzle[y][x] == '.':
        puzzle[y][x] = 'W'
        direction -= 1
    else:
        puzzle[y][x] = '#'
        solution += 1

    x += move[direction % 4][1]
    y += move[direction % 4][0]
    if x == max_x:
        max_x += 1
        for line in puzzle:
            line.append('.')
    if y == max_y:
        new_line = ['.'] * max_x
        puzzle.append(new_line[:])
        max_y += 1
    if x < 0:
        for line in puzzle:
            line.insert(0, '.')
        x = 0
        max_x += 1
    if y < 0:
        new_line = ['.'] * max_x
        puzzle.insert(0, new_line[:])
        y = 0
        max_y += 1
print(solution)
