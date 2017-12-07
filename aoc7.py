with open('aoc7.txt') as f:
    file_ = [line.split() for line in f]

solution = []
structure = {}
test = []

for program in file_:
    if len(program) == 2:
        structure[program[0]] = [int(program[1].strip('()')), []]
    elif len(program) > 2:
        structure[program[0]] = (int(program[1].strip('()')), [program[x].strip(',') for x in range(3, len(program))])
        for x in range(3, len(program)):
            test.append(program[x].strip(','))

for program in file_:
    if len(program) > 2 and program[0] not in test:
        #pass
        solution = program[0]
        print("part one: {}".format(program[0]))

pillars = [x for x in structure[solution][1]]

weight = []

def add_weight(thing):
    for x in structure[thing][1]:
        weight[-1] += int(structure[x][0])
        add_weight(x)

for x in pillars:
    weight.append(0)
    check = weight[-1]
    weight[-1] += structure[x][0]
    # while weight[-1] != check:
    #     check = weight[-1]
    add_weight(x)
        # for y in structure[x][1]:
        #     weight[-1] += structure[y][0]

print(weight)
print(pillars)
