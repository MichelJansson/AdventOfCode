import os
import math

inputfile = os.path.dirname(__file__) + "\\input.txt"

# Init data
heightmap = [[int(z) for z in list(y)] for y in [x.strip() for x in open(inputfile).readlines()]]

visited = []
basins = [[]]

def checkNeighbours(rowi, coli):
    if (rowi, coli) in visited:
        return
    
    visited.append((rowi, coli))

    current = heightmap[rowi][coli]
    if current == 9:
        return

    basins[-1].append(current)

    if rowi > 0:
        checkNeighbours(rowi-1, coli) #up
    if rowi < len(heightmap)-1:
        checkNeighbours(rowi+1, coli) #down
    if coli > 0:
        checkNeighbours(rowi, coli-1) #left
    if coli < len(heightmap[rowi])-1:
        checkNeighbours(rowi, coli+1) #right

for rowi in range(len(heightmap)):
    print(heightmap[rowi])
    for coli in range(len(heightmap[rowi])):
        if len(basins[-1]) > 0:
            basins.append([])
        checkNeighbours(rowi, coli)

basins.sort(key=len)

threeLargestBasinsProducts = math.prod([len(x) for x in basins[-3:]])

answer = threeLargestBasinsProducts
print("Day9, part2, answer:", answer)
