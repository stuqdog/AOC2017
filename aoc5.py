with open('aoc5.txt') as f:
    directions = [int(line.strip('\n')) for line in f]

end_point = len(directions)
current_direction = 0
steps = 0

while current_direction < end_point:
    directions[current_direction] += 1
    current_direction += directions[current_direction] - 1
    steps += 1

print(steps)
