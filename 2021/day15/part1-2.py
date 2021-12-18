import os
import math
from collections import defaultdict

inputfile = os.path.dirname(__file__) + "\\input.txt"

# startpos, goalpos, heuristic function, distance function
def aStar(width, height, start, goal, h, d):
    directions = [(0,1), (1,0), (-1,0), (0,-1)] # D, R, L, U

    openSet = {} # {pos: fScore}
    openSet[start] = h(start)

    cameFrom = {}

    gScore = defaultdict(lambda: math.inf)
    gScore[start] = 0

    fScore = defaultdict(lambda: math.inf)
    fScore[start] = h(start)

    while len(openSet) > 0:
        current = min(openSet, key=openSet.get) # min fScore

        if current == goal:
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            return list(reversed(path))

        openSet.pop(current)

        for dir in directions:
            x = current[0]+dir[0]
            y = current[1]+dir[1]

            if 0<=x<width and 0<=y<height: # within bounds
                neighbor = (x, y)

                tentative_gScore = gScore[current] + d(current, neighbor) # current gScore + distance
                if tentative_gScore < gScore[neighbor]:
                    # This path to neighbor is better than any previous one. Record it!
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = tentative_gScore + h(neighbor)

                    openSet[neighbor] = fScore[neighbor] #fscore

    assert False

# Init data
riskMap = [[int(z) for z in list(y)] for y in [x.strip() for x in open(inputfile)]]

rows = len(riskMap)
cols = len(riskMap[0])

def heuristic(node):
    return 0 #manhattan distance is apparenly a poor heuristic so it's not used.

def distance(current, neighbor):
    # in part 2, the risks are increased for each tile away from origin
    # which is why this extra work is done here, but it has no effect on part 1
    col = neighbor[0] % cols
    row = neighbor[1] % rows
    riskOffset = neighbor[0] // cols + neighbor[1] // rows
    risk = riskMap[row][col] + riskOffset
    return risk if risk<10 else risk-9

def calcTotalRisk(path):
    totalRisk = 0
    for point in path:
        if point == (0,0): continue # ignore first risk, per description
        totalRisk += distance(None, point)
    return totalRisk

path = aStar(rows, cols, (0,0), (cols-1,rows-1), heuristic, distance)
print("Day15, part1, answer:", calcTotalRisk(path))

part2rows = rows * 5
part2cols = cols * 5
path = aStar(part2rows, part2cols, (0,0), (part2rows-1,part2cols-1), heuristic, distance)
print("Day15, part2, answer:", calcTotalRisk(path))
