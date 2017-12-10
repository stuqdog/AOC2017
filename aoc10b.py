instructions = [ord(x) for x in "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229"]
instructions += [17,31,73,47,23]

order = list(range(256))

skip_size = 0
point = 0

for rounds in range(64):
    for x in instructions:
        for y in range(x // 2):
            order[(point + y) % 256], order[(point + x - y - 1) % 256] = (
            order[(point + x - y - 1) % 256], order[(point + y) % 256])
        point += (skip_size + x)
        skip_size += 1

short_hash = [0] * 16

for x in range(16):
    for y in range(16):
        short_hash[x] ^= order[x * 16 + y]

print(''.join([hex(x).strip('0x') if len(hex(x)) == 4 else '0' + hex(x).strip('0x') for x in short_hash]))
