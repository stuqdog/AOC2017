'''Note to self: come back to this one. Significant refactoring is def possible,
would be a worthwhile project to figure out how to make this better.'''

with open('aoc19.txt') as f:
    puzzle = [line for line in f]

direction = 'down'
solution = ''
solution_two = 0

y = 0
x = puzzle[0].index('|')
solution_two = 0

while True:
    solution_two += 1
    if puzzle[y][x].isalpha():
        solution += puzzle[y][x]
        
    if direction == 'down':
        if puzzle[y+1][x] != ' ':
            y += 1
        elif puzzle[y][x+1] != ' ':
            x += 1
            direction = 'right'
        elif puzzle[y][x-1] != ' ':
            x -= 1
            direction = 'left'
        else:
            break

    elif direction == 'left':
        if puzzle[y][x-1] != ' ':
            x -= 1
        elif puzzle[y+1][x] != ' ':
            y += 1
            direction = 'down'
        elif puzzle[y-1][x] != ' ':
            y -= 1
            direction = 'up'
        else:
            break

    elif direction == 'up':
        if puzzle[y-1][x] != ' ':
            y -= 1
        elif puzzle[y][x+1] != ' ':
            x += 1
            direction = 'right'
        elif puzzle[y][x-1] != ' ':
            x -= 1
            direction = 'left'
        else:
            break

    elif direction == 'right':
        if puzzle[y][x+1] != ' ':
            x += 1
        elif puzzle[y+1][x] != ' ':
            y += 1
            direction = 'down'
        elif puzzle[y-1][x] != ' ':
            y -= 1
            direction = 'up'
        else:
            break
            
print("Part one: {}\nPart two: {}".format(solution, solution_two))
