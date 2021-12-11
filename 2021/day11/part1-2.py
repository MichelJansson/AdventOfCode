import os
import queue

inputfile = os.path.dirname(__file__) + "\\input.txt"

# Init data
octopuses = [[int(z) for z in list(y)] for y in [x.strip() for x in open(inputfile).readlines()]]

rows = len(octopuses)
cols = len(octopuses[0])

#        T  TR  R  BR B   BL  L   TL
dirY = [-1, -1, 0, 1, 1,  1,  0, -1]
dirX = [ 0,  1, 1, 1, 0, -1, -1, -1]

totalflashes = 0
step100flashes = None
syncStep = None
for step in range(1, 1000):
    stepflashes = 0

    # increase all energy by 1
    for rowi in range(rows):
        for coli in range(cols):
            octopuses[rowi][coli] += 1

    # step2
    rippleQueue = queue.Queue()
    for rowi in range(rows):
        for coli in range(cols):
            if octopuses[rowi][coli] > 9:
                rippleQueue.put((rowi, coli))

    while True:
        if rippleQueue.empty():
            break

        crowi, ccoli = rippleQueue.get()
        if octopuses[crowi][ccoli] == 0: # flahsed some other time "out of order"
            continue

        octopuses[crowi][ccoli] = 0
        totalflashes += 1
        stepflashes += 1

        # check and updated all adjacents (bfs)
        for dir in range(8):
            # adjecent row/col
            arowi = crowi + dirY[dir]
            acoli = ccoli + dirX[dir]

            if 0<=arowi<rows and 0<=acoli<cols and octopuses[arowi][acoli] != 0:
                octopuses[arowi][acoli] += 1
                if octopuses[arowi][acoli] > 9:
                    rippleQueue.put((arowi, acoli))

    print("After step:", step)
    for rowi in range(rows):
        print(octopuses[rowi])

    if step == 100:
        step100flashes = totalflashes

    if stepflashes == rows * cols:
        syncStep = step
        break

print("Day10, part1, answer:", step100flashes)
print("Day10, part2, answer:", syncStep)
