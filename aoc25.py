from collections import Counter

state = 'A'
ticker = Counter()
x = 0

for y in range(12861455):
    if state == 'A':
        ticker[x] = -ticker[x] + 1
        if ticker[x]:
            x += 1
        else:
            x -= 1
        state = 'B'

    elif state == 'B':
        ticker[x] = -ticker[x] + 1
        if ticker[x]:
            x -= 1
            state = 'C'
        else:
            x += 1
            state = 'E'

    elif state == 'C':
        ticker[x] = -ticker[x] + 1
        if ticker[x]:
            state = 'E'
            x += 1
        else:
            x -= 1
            state = 'D'

    elif state == 'D':
        ticker[x] = 1
        x -= 1
        state = 'A'

    elif state == 'E':
        state = 'F' if ticker[x] else 'A'
        ticker[x] = 0
        x += 1

    elif state == 'F':
        state = 'A' if ticker[x] else 'E'
        ticker[x] = 1
        x += 1

print(sum(ticker[x] for x in ticker))
