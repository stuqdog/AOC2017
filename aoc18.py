from collections import Counter

with open('aoc18.txt') as f:
    instr = [line.strip() for line in f]

class Register():

    instr = instr
    length = len(instr)

    def __init__(self, p):
        self.x = 0
        self.regs = Counter()
        self.regs['p'] = p
        self.queue = []
        self.is_one = p

    def follow_instruction(self, receiver):

        if self.x not in range(Register.length):
            return True

        line = Register.instr[self.x].split()

        if line[0] == 'snd':
            receiver.queue.append(self.regs[line[1]])
            if self.is_one:
                self.is_one += 1

        elif line[0] == 'set':
            self.regs[line[1]] = self.regs[line[2]] if line[2].isalpha() else int(line[2])

        elif line[0] == 'add':
            self.regs[line[1]] += self.regs[line[2]] if line[2].isalpha() else int(line[2])

        elif line[0] == 'mul':
            self.regs[line[1]] *= self.regs[line[2]] if line[2].isalpha() else int(line[2])

        elif line[0] == 'mod':
            self.regs[line[1]] %= self.regs[line[2]] if line[2].isalpha() else int(line[2])

        elif line[0] == 'rcv':
            if self.queue:
                self.regs[line[1]] = self.queue[0]
                del self.queue[0]
            else:
                return True

        elif line[0] == "jgz":
            if line[1].isalpha():
                if self.regs[line[1]] > 0:
                    self.x += self.regs[line[2]] if line[2].isalpha() else int(line[2])
                    self.x -=1
            elif int(line[1]) > 0:
                self.x += self.regs[line[2]] if line[2].isalpha() else int(line[2])
                self.x -= 1
        self.x += 1
        return False


def part_one(instr):
    x = 0
    regs = Counter()
    while x < len(instr):
        line = instr[x].split()
        if line[0] == "snd":
            sounds = regs[line[1]] if line[1].isalpha() else int(line[1])

        elif line[0] == 'set':
            regs[line[1]] = regs[line[2]] if line[2].isalpha() else int(line[2])

        elif line[0] == 'add':
            regs[line[1]] += regs[line[2]] if line[2].isalpha() else int(line[2])

        elif line[0] == 'mul':
            regs[line[1]] *= regs[line[2]] if line[2].isalpha() else int(line[2])

        elif line[0] == 'mod':
            regs[line[1]] %= regs[line[2]] if line[2].isalpha() else int(line[2])

        elif line[0] == 'rcv':
            if line[1] != '0':
                return(sounds)

        else:
            if line[1].isalpha():
                if regs[line[1]] > 0:
                    x += regs[line[2]] if line[2].isalpha() else int(line[2])
                    x -=1
            elif int(line[1]) > 0:
                x += regs[line[2]] if line[2].isalpha() else int(line[2])
                x -= 1
        x += 1

print("Part one: {}".format(part_one(instr)))

regs_one = Register(0)
regs_two = Register(1)

while True:
    if regs_one.follow_instruction(regs_two) and regs_two.follow_instruction(regs_one):
        break

print("Part two: {}".format(regs_two.is_one - 1))
