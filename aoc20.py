class Thing():
    def __init__(self, a, v, s, line=0):
        self.a = a
        self.v = v
        self.s = s
        self.line = line

def part_one(instr):
    line_num = 0
    solution = Thing(1000000, 10000000, 10000000)

    for line in instr:
        s = line[0].split('=')[1].strip("<>,")
        s = map(int, s.split(','))
        s = sum(abs(x) for x in s)
        v = line[1].split('=')[1].strip("<>,")
        v = map(int, v.split(','))
        v = sum(abs(x) for x in v)
        a = line[2].split('=')[1].strip("<>,")
        a = map(int, a.split(','))
        a = sum(abs(x) for x in a)

        check = Thing(a, v, s, line_num)
        if abs(a) < abs(solution.a):
            solution = Thing(a, v, s, line_num)
        line_num += 1
    return(solution.line)


def part_two(instr):
    '''A bit of a brute force solution, unfortunately. Just loops until the same
    number keeps showing up over and over. I'm sure there's a better way to do
    this... would be fun to research it!'''
    particles = []

    for line in instr:
        s = line[0].split('=')[1].strip("<>,")
        s =  list(map(int, s.split(',')))
        v = line[1].split('=')[1].strip("<>,")
        v = list(map(int, v.split(',')))
        a = line[2].split('=')[1].strip("<>,")
        a = list(map(int, a.split(',')))
        particles.append(Thing(a, v, s))

    repetitions = 0
    for encounter in range(10000):
        delete = []
        for particle in particles:
            for xyz in range(3):
                particle.v[xyz] += particle.a[xyz]
                particle.s[xyz] += particle.v[xyz]
        for i, particle in enumerate(particles):
            for i_, particle_ in enumerate(particles[i+1:]):
                if particle.s == particle_.s:
                    delete.append(i)
                    delete.append(i+i_+1)
        delete = sorted(list(set(delete)), reverse=True)
        for i in delete:
            del particles[i]
        if delete:
            repetitions = 0
        else:
            repetitions += 1
            if repetitions >= 15:
                return(len(particles))

with open('aoc20.txt') as f:
    instr = [line.strip().split() for line in f]

print("Part one: {}".format(part_one(instr)))
print("Part two: {}".format(part_two(instr))) # Takes about three seconds.
