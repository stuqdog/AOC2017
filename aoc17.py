puzzle = [0]
current = 0
p_two = 0

for x in range(1, 2018):
    current = (current + 356) % x + 1
    puzzle.insert(current, x)

solution = puzzle.index(2017) + 1
print("Part one: {}".format(puzzle[solution]))

for x in range(1, 50_000_001):
    p_two = (p_two + 356) % x + 1
    if p_two == 1:
        solution = x

print("Part two: {}".format(solution))
