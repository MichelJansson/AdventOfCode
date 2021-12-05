input = open("day3\\input.txt", "r")
lines = [line.rstrip() for line in input.readlines()]
input.close()

linelengh = len(lines[0])

gamma_rate_bits = '0b'
epsilon_rate_bits = '0b'

for bitpos in range(linelengh):
    ones = 0
    zeros = 0
    
    for line in lines:
        if line[bitpos] == "1":
            ones += 1
        else:
            zeros += 1
    
    if ones > zeros:
        gamma_rate_bits += '1'
        epsilon_rate_bits += '0'
    else:
        gamma_rate_bits += '0'
        epsilon_rate_bits += '1'

gamma_rate = int(gamma_rate_bits, 2)
epsilon_rate = int(epsilon_rate_bits, 2)

print("Day3, Part1 answer: " + str(gamma_rate * epsilon_rate))