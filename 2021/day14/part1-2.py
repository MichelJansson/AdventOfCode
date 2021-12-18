import os
from collections import defaultdict

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

polymerPairs = defaultdict(int)
for i in range(len(template)-1):
    polymerPairs[template[i]+template[i+1]] += 1
#print("Template:", polymerPairs)

elementCount = defaultdict(int)
for char in template:
    elementCount[char] += 1

def calcAnswer():
    mostCommon = max(elementCount.items(), key = lambda elementCount : elementCount[1])
    leastCommon = min(elementCount.items(), key = lambda elementCount : elementCount[1])
    print("Most common:", mostCommon, "Least common:", leastCommon)
    return mostCommon[1] - leastCommon[1]

for stepi in range(1, 40+1):
    lastPolymerPairs = polymerPairs
    polymerPairs = defaultdict(int)

    for pair in lastPolymerPairs.keys():
        insertion = insertionRules[pair]
        if insertion:
            pairCount = lastPolymerPairs[pair]
            elementCount[insertion] += pairCount
            # build new (overlapping) pairs
            polymerPairs[pair[0]+insertion] += pairCount
            polymerPairs[insertion+pair[1]] += pairCount

    #print("After step", stepi, polymerPairs)
    #print("After step", stepi, charCount)
    if (stepi == 10):
        print("Day14, part1, answer:", calcAnswer())

print("Day14, part2, answer:", calcAnswer())
