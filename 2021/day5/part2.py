import os
from collections import defaultdict

inputfile = os.path.dirname(__file__) + "\\input.txt"

points_visited = defaultdict(int)

for line in open(inputfile):
    line = line.strip()

    # [x1, y1], [x2, y2]
    p1, p2 = [[int(x) for x in p.split(',')] for p in line.split(' -> ')]

    xdiff = p2[0] - p1[0]
    ydiff = p2[1] - p1[1]

    # since we only can support exact 45's assert the diff is the same
    if abs(xdiff) > 0 and abs(ydiff) > 0:
        assert abs(xdiff) == abs(ydiff)

    xpos = p1[0]
    ypos = p1[1]
    steps = max(abs(xdiff), abs(ydiff)) + 1
    for i in range(steps):
        if i > 0: # dont count on first step
            if xdiff > 0:
                xpos += 1
            elif xdiff < 0:
                xpos -= 1
            if ydiff > 0:
                ypos += 1
            elif ydiff < 0:
                ypos -= 1

        points_visited[(xpos, ypos)] += 1

answer = 0
for count in points_visited.values():
    if count > 1:
        answer += 1

print("Day5, Part2 Answer: ", answer)
