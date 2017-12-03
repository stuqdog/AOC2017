from sys import exit

grid = {(0, 0): 1}
x_diff = 0
y_diff = 0
step = 0
target = 265149

def surrounding_cells_array(coordinates):
    x, y = coordinates
    return [(x+1,y+1), (x+1,y), (x+1, y-1), (x,y+1), (x,y-1), (x-1,y+1), (x-1, y), (x-1, y-1)]

def determine_coordinate_value(coordinates):
    grid[coordinates] = sum(grid[x] for x in
          surrounding_cells_array(coordinates) if x in grid)
    if grid[coordinates] > target:
        print(grid[coordinates])
        exit()

while True:
    step += 1
    for x in range(step):
        x_diff += 1
        determine_coordinate_value((x_diff, y_diff))
    for y in range(step):
        y_diff += 1
        determine_coordinate_value((x_diff, y_diff))

    step += 1
    for x in range(step):
        x_diff -= 1
        determine_coordinate_value((x_diff, y_diff))
    for y in range(step):
        y_diff -= 1
        determine_coordinate_value((x_diff, y_diff))
