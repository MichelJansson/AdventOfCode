import os
from collections import defaultdict

inputfile = os.path.dirname(__file__) + "\\input.txt"

# Init data
fishes = [int(x) for x in open(inputfile).readline().strip().split(',')]

evolution = defaultdict(int)
for fish in fishes:
    evolution[fish] += 1

for dayi in range(256):
    newevolution = defaultdict(int)

    newevolution[8] = evolution[0]
    newevolution[7] = evolution[8]
    newevolution[6] = evolution[7] + evolution[0]
    newevolution[5] = evolution[6]
    newevolution[4] = evolution[5]
    newevolution[3] = evolution[4]
    newevolution[2] = evolution[3]
    newevolution[1] = evolution[2]
    newevolution[0] = evolution[1]

    evolution = newevolution

answer = sum(evolution.values())
print("Day6, Part2 Answer: ", answer)
