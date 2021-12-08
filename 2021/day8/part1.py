import os
from collections import defaultdict

inputfile = os.path.dirname(__file__) + "\\input.txt"

lendigitmap = {
    0: None,
    1: None,
    2: 1,
    3: 7,
    4: 4,
    5: None,
    6: None,
    7: 8,
}

digitcount = defaultdict(int)
for line in open(inputfile):
    signalpattern, digitoutput = line.strip().split('|')
    signalpattern = signalpattern.strip().split()
    digitoutput = digitoutput.strip().split()

    for scrableddigit in digitoutput:
        digit = lendigitmap[len(scrableddigit)]
        if digit:
            digitcount[digit] += 1

answer = sum(digitcount.values())
print("Day8, Part1 Answer:", answer)

