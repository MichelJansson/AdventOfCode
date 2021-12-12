import os
from collections import defaultdict

inputfile = os.path.dirname(__file__) + "\\input.txt"

caveMap = defaultdict(list)

# Init data
for line in open(inputfile).readlines():
    cavePair = line.strip().split('-')
    caveMap[cavePair[0]].append(cavePair[1])
    caveMap[cavePair[1]].append(cavePair[0])

# function to explore a cave depth first to find all possible paths
def exploreCaveDf(cave, path, allowSingleSmallTwice=False, twiceOn=None):
    newpaths = 0
    for node in sorted(caveMap[cave]):
        newtwiceOn = twiceOn # needs to be reset for each node
        if node == cave or node == 'start':
            continue # dont explore backwards
        if node == 'end':
            newpaths += 1
            #print("Path found: start ->", path, "-> end")
            continue
        if node.islower() and node in path:
            if allowSingleSmallTwice and not twiceOn:
                # in part2 we can allow a single small cave to be visited twice
                # within the entire path. Here we take the oppertunity and registers it.
                newtwiceOn = node 
            else:
                continue # small cave not allowed to be visited again

        newpath = path.copy()
        newpath.append(node)
        newpaths += exploreCaveDf(node, newpath, allowSingleSmallTwice, newtwiceOn)
    return newpaths

paths1 = exploreCaveDf('start', [])
paths2 = exploreCaveDf('start', [], True)

print("Day12, part1, answer:", paths1)
print("Day12, part2, answer:", paths2)
