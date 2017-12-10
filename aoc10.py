instructions = [int(x) for x in "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229".split(',')]

order = list(range(256))

skip_size = 0
point = 0

for x in instructions:
    for y in range(x // 2):
        order[(point + y) % 256], order[(point + x - y - 1) % 256] = (
        order[(point + x - y - 1) % 256], order[(point + y) % 256])
    point += (skip_size + x)
    skip_size += 1
print(order[0] * order[1])
