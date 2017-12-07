with open('aoc7.txt') as f:
    file_ = [line.split() for line in f]

solution = []
structure = {}
test = []

for program in file_:
    if len(program) == 2:
        structure[(program[0], program[1])] = []
        test.append(program[0])
    elif len(program) > 2:
        structure[(program[0], program[0])] = [program[x].strip(',') for x in range(3, len(program))]
        for x in range(3, len(program)):
            test.append(program[x].strip(','))

for program in file_:
    if len(program) > 2 and program[0] not in test:
        #pass
        solution.append(program[0])
        print("part one: {}".format(program[0]))
