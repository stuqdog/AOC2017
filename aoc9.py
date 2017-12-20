from collections import Counter

with open('aoc9.txt') as f:
    puzzle = str([line for line in f][0])

end = len(puzzle)
i = 0
openings = []
summary = Counter()
garbage = False
garbage_count = 0

while i < end:
    if puzzle[i] == '{' and garbage == False:
        openings.append(1)
    elif puzzle[i] == '}' and garbage == False:
        summary[len(openings)] += 1
        del(openings[-1])
    elif puzzle[i] == '<' and garbage == False:
        garbage = True
    elif puzzle[i] == '>' and garbage == True:
        garbage = False
    elif garbage == True and puzzle[i] == '!':
        i += 1
    elif garbage == True:
        garbage_count += 1
    i += 1

print("part one: {}".format(sum(summary[x] * x for x in summary)))
print("part two: {}".format(garbage_count))
