with open('aoc19.txt') as f:
    puzzle = [line for line in f]

direction = 'down'
solution = ''
solution_two = 0

y = 0
x = puzzle[0].index('|')
y_max = len(puzzle)
x_max = len(puzzle[0])
solution_two = 0

while True:
    solution_two += 1
    if puzzle[y][x].isalpha():
        solution += puzzle[y][x]
        
    if direction == 'down':
        if (y+1) in range(y_max) and puzzle[y+1][x] != ' ':
            y += 1
        elif (x+1) in range(x_max) and puzzle[y][x+1] != ' ':
            x += 1
            direction = 'right'
        elif x > 0 and puzzle[y][x-1] != ' ':
            x -= 1
            direction = 'left'
        else:
            break

    elif direction == 'left':
        if  x > 0 and puzzle[y][x-1] != ' ':
            x -= 1
        elif (y+1) in range(y_max) and puzzle[y+1][x] != ' ':
            y += 1
            direction = 'down'
        elif y > 0 and puzzle[y-1][x] != ' ':
            y -= 1
            direction = 'up'
        else:
            break

    elif direction == 'up':
        if y > 0 and puzzle[y-1][x] != ' ':
            y -= 1
        elif (x+1) in range(x_max) and puzzle[y][x+1] != ' ':
            x += 1
            direction = 'right'
        elif x > 0 and puzzle[y][x-1] != ' ':
            x -= 1
            direction = 'left'
        else:
            break

    elif direction == 'right':
        if (x+1) in range(x_max) and puzzle[y][x+1] != ' ':
            x += 1
        elif (y+1) in range(y_max) and puzzle[y+1][x] != ' ':
            y += 1
            direction = 'down'
        elif y > 0 and puzzle[y-1][x] != ' ':
            y -= 1
            direction = 'up'
        else:
            break
            
print("Part one: {}\nPart two: {}".format(solution, solution_two))
