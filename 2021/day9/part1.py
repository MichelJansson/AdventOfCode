import os
import math

inputfile = os.path.dirname(__file__) + "\\input.txt"

# Init data
heightmap = [[int(z) for z in list(y)] for y in [x.strip() for x in open(inputfile).readlines()]]

lowpoints = []

for rowi in range(len(heightmap)):
    print(heightmap[rowi])

    for coli in range(len(heightmap[rowi])):
        current = heightmap[rowi][coli]
        up =    heightmap[rowi-1][coli] if rowi > 0 else math.inf
        down =  heightmap[rowi+1][coli] if rowi < len(heightmap)-1 else math.inf
        left =  heightmap[rowi][coli-1] if coli > 0 else math.inf
        right = heightmap[rowi][coli+1] if coli < len(heightmap[rowi])-1 else math.inf

        if current < up and current < down and current < left and current < right:
            lowpoints.append(current)

risklevels = sum(lowpoints) + len(lowpoints)
answer = risklevels
print("Day9, part1, answer:", answer)
