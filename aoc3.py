x_diff, y_diff = 0, 0
target = 265149
current = 1
step = 0

while True:
    step += 1
    x_diff, current = x_diff + step, current + step
    if current >= target:
        x_diff -= current - target
        break
    y_diff, current = y_diff + step, current + step
    if current >= target:
        y_diff -= current - target
        break
    step += 1
    x_diff, current = x_diff - step, current + step
    if current >= target:
        x_diff += current - target
        break
    y_diff, current = y_diff - step, current + step
    if current >= target:
        y_diff += current - target
        break

print(abs(x_diff) + abs(y_diff))
