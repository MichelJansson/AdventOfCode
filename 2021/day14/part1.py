import os
from collections import Counter

inputfile = os.path.dirname(__file__) + "\\input.txt"

# Init data
template = None
insertionRules = {}
for line in open(inputfile):
    line = line.strip()

    if not line: continue
    elif not template:
        template = line
        continue

    insertion = line.split(' -> ')
    insertionRules[insertion[0]] = insertion[1]

polymerChain = []
for char in template:
    polymerChain.append(char)

print("Template:", polymerChain)

for stepi in range(1, 10+1):
    lastPolymerChain = polymerChain
    polymerChain = []

    for i in range(len(lastPolymerChain)-1):
        polymerChain.append(lastPolymerChain[i])
        polymerChain.append(insertionRules[lastPolymerChain[i] + lastPolymerChain[i+1]])
    
    polymerChain.append(lastPolymerChain[i+1])
    #print("After step", stepi, polymerChain)

polymerCounter = Counter(polymerChain)
mostCommon = polymerCounter.most_common()
print("Most common:", mostCommon[0], "Least common:", mostCommon[-1])

answer = mostCommon[0][1] - mostCommon[-1][1]
print("Day14, part1, answer:", answer)

# This algo could not handle the size of the data generated of part2, and had
# to be solved in anoter way. part1-2.py solves this and solves both parts too.
