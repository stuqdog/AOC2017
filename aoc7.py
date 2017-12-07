from collections import Counter

with open('aoc7.txt') as f:
    file_ = [line.split() for line in f]

solution = []
solution_two = 0
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


def create_pillars(base):
    pillars = [x for x in structure[base][1]]
    weight = []
    for x in pillars:
        weight.append(0)
        weight[-1] += structure[x][0]
        weight, possible_solution = add_weight(x, weight)
    print(pillars)
    return pillars, weight, possible_solution

def add_weight(thing, weight_sub):
    for x in structure[thing][1]:
        weight_sub[-1] += int(structure[x][0])
        add_weight(x, weight_sub)
    possible_solution = Counter(weight_sub)
    return weight_sub, possible_solution

pillars, weight, possible_solution = create_pillars(solution)
print(pillars)
print(weight)


while len(set(weight)) == 2:
    for num in weight:

        if Counter(weight)[num] == 1:
            index = weight.index(num)
            break

    pillars, weight, possible_solution = create_pillars(pillars[index])
print(possible_solution)
