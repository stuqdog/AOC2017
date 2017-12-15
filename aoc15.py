gen_a = 634
gen_b = 301

matches = 0
x = 0

# for x in range(40000000): <-- Part one!
for x in range(40000000): # <-- Part two!
    gen_a *= 16807
    gen_a %= 2147483647
    gen_b *= 48271
    gen_b %= 2147483647

## Part two only below!
    # while gen_a % 4 != 0:
    #     gen_a *= 16807
    #     gen_a %= 2147483647
    # while gen_b % 8 != 0:
    #     gen_b *= 48271
    #     gen_b %= 2147483647
## Part two only above!

    if bin(gen_a)[-16:] == bin(gen_b)[-16:]:
        matches += 1

print(matches)
