with open("aoc1.txt") as f:
    for line in f:
        print(sum(int(c) for i, c in enumerate(line) if c == line[(i + 1) % len(line.strip())]))
