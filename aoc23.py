from collections import Counter

def main(start, instr):
    regs = Counter()
    regs['a'] = start
    x=0
    pt1 = 0
    while x in range(len(instr)):

        line = instr[x]
        if line[0] == 'set':
            regs[line[1]] = regs[line[2]] if line[2].isalpha() else int(line[2])

        elif line[0] == 'sub':
            regs[line[1]] -= regs[line[2]] if line[2].isalpha() else int(line[2])

        elif line[0] == 'mul':
            regs[line[1]] *= regs[line[2]] if line[2].isalpha() else int(line[2])
            pt1 += 1

        elif line[0] == "jnz":
            if line[1].isalpha():
                if regs[line[1]] != 0:
                    x += regs[line[2]] if line[2].isalpha() else int(line[2])
                    x -=1
            elif int(line[1]) > 0:
                x += regs[line[2]] if line[2].isalpha() else int(line[2])
                x -= 1

        x += 1

        '''The two below chunks (if x == 19 and if x == 23) basically summarize the
        crazy long loops that occur when x hits 19 or 23.'''
        if x == 19 and start == 1:
            regs['g'] = regs['d'] * regs['e'] - regs['b']
            regs['e'] += (regs['b'] - regs['e']) + 1
            regs['g'] = 0
            x += 1

        if x == 23 and start == 1:
            regs['e'] = 2
            regs['g'] = regs['e'] * regs['d'] - regs['b']
            if any(regs['b'] % d == 0 for d in range(regs['d'], regs['d'] - regs['g'])):
                regs['f'] = 0
            regs['d'] -= regs['g']
            regs['g'] = 0
            x += 1
    return pt1, regs

with open('aoc23.txt') as f:
    instr = [line.strip().split() for line in f]

pt1, meh = main(0, instr)
meh, pt2 = main(1, instr)
print("Part one:", pt1)
print("Part two:", pt2['h']) #Takes about 4sec to solve
