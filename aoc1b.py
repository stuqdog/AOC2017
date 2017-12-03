with open("aoc1.txt") as f:
    for line in f:
        print(sum(int(c) for i, c in enumerate(line) if c
              == line[(i + (len(line.strip()) // 2)) % len(line.strip())]))
