with open("aoc4.txt") as f:
    print(sum(1 for line in f if len(line.split()) == len(set(line.split()))))
