input = open("day3\\input.txt", "r")
lines = [line.rstrip() for line in input.readlines()]
input.close()

linelengh = len(lines[0])

oxy_bit_criteria = ''
co2_bit_criteria = ''

oxy_rate_bits = ''
co2_rate_bits = ''

for bitpos in range(linelengh):
    oxy_ones = 0
    oxy_zeros = 0
    co2_ones = 0
    co2_zeros = 0
    
    for line in lines:
        if bitpos == 0 or line.startswith(oxy_bit_criteria):
            oxy_rate_bits = line
            if line[bitpos] == "1":
                oxy_ones += 1
            else:
                oxy_zeros += 1

        if bitpos == 0 or line.startswith(co2_bit_criteria):
            co2_rate_bits = line
            if line[bitpos] == "1":
                co2_ones += 1
            else:
                co2_zeros += 1

    if oxy_ones >= oxy_zeros:
        oxy_bit_criteria += '1'
    else:
        oxy_bit_criteria += '0'

    if co2_ones >= co2_zeros:
        co2_bit_criteria += '0'
    else:
        co2_bit_criteria += '1'


oxy_rate = int('0b' + oxy_rate_bits, 2)
co2_rate = int('0b' + co2_rate_bits, 2)

print("Day3, Part2 answer: " + str(oxy_rate * co2_rate))