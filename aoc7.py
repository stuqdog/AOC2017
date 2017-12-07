from collections import Counter

with open('aoc7.txt') as f:
    file_ = [line.split() for line in f]

structure = {}
test = []

for program in file_:
    if len(program) == 2:
        structure[program[0]] = [int(program[1].strip('()')), []]
    elif len(program) > 2:
        structure[program[0]] = (int(program[1].strip('()')), [program[x].strip(',')
                                 for x in range(3, len(program))])
        for x in range(3, len(program)):
            test.append(program[x].strip(','))

for program in file_:
    if len(program) > 2 and program[0] not in test:
        solution = program[0]
        print("part one: {}".format(solution))

pillars = [x for x in structure[solution][1]]
weight = []
possible_solution = 0

def create_pillars(base, possible_solution):
    pillars = [x for x in structure[base][1]]
    weight = []
    for x in pillars:
        weight.append(0)
        weight[-1] += structure[x][0]
        weight, possible_solution = add_weight(x, weight, possible_solution)
    print(pillars)
    return pillars, weight, possible_solution

def add_weight(thing, weight_sub, possible_solution):
    for x in structure[thing][1]:
        weight_sub[-1] += int(structure[x][0])
        add_weight(x, weight_sub, possible_solution)
    if any(weight_sub[x] != weight_sub[0] for x in range(len(weight_sub))):
        possible_solution = thing
    return weight_sub, possible_solution

pillars, weight, possible_solution = create_pillars(solution, possible_solution)
print(pillars)
print(weight)


while len(set(weight)) == 2:
    for num in weight:

        if Counter(weight)[num] == 1:
            index = weight.index(num)
            break

    pillars, weight, possible_solution = create_pillars(pillars[index], possible_solution)
print(possible_solution)
for x in structure:
    if possible_solution in structure[x][1]:
        print([structure[y][0] for y in structure[x][1]])
