import os

inputfile = os.path.dirname(__file__) + "\\input.txt"

linecords = []

# Init data
for line in open(inputfile):
    line = line.strip()

    # [[x1, y1], [x2, y2]]
    linecord = [[int(x) for x in ends.split(',')] for ends in line.split(' -> ')]

    # only consider horizontal and vertical line
    if linecord[0][0] != linecord[1][0] and linecord[0][1] != linecord[1][1]:
        continue

    linecords.append(linecord)

visited_cords = {}
linemap = []

# plot
for linecord in linecords:
    xdiff = linecord[0][0] - linecord[1][0]
    ydiff = linecord[0][1] - linecord[1][1]

    if abs(xdiff) > 0:
        xpos = linecord[0][0]
        for xmove in range(abs(xdiff) + 1):
            if xmove > 0: # dont count on first
                if xdiff < 0:
                    xpos += 1
                else:
                    xpos -= 1

            strCord = str([xpos, linecord[0][1]])
            if strCord in visited_cords:
                visited_cords[strCord] += 1
            else:
                visited_cords[strCord] = 1

    elif abs(ydiff) > 0:
        ypos = linecord[0][1]
        for ymove in range(abs(ydiff) + 1):
            if ymove > 0: # dont count on first
                if ydiff < 0:
                    ypos += 1
                else:
                    ypos -= 1

            strCord = str([linecord[0][0], ypos])
            if strCord in visited_cords:
                visited_cords[strCord] += 1
            else:
                visited_cords[strCord] = 1

countmorethatone = 0
for count in visited_cords.values():
    if count > 1:
        countmorethatone += 1


print(visited_cords)

print("Day5, Part1 Answer: " + str(countmorethatone))
