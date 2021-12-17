import os

inputfile = os.path.dirname(__file__) + "\\input.txt"

# Init data
dotVerticies = []
foldInstructions = [] # (foldAxis, foldAlong)
rows = 0
cols = 0
for line in open(inputfile):
    line = line.strip()
    if not line:
        continue
    elif line.startswith("fold"):
        foldAxis = "x" if "x=" in line else "y"
        foldAlong = int(line.split("=")[1])
        foldInstructions.append((foldAxis, foldAlong))
    else:
        vertex = [int(x) for x in line.split(',')]
        if vertex[0] > cols:
            cols = vertex[0]
        if vertex[1] > rows:
            rows = vertex[1]
        dotVerticies.append(vertex)

# Init sheet (2d matrix)
dotCount = len(dotVerticies)
rows += 1
cols += 1
sheet = [ [' ']*(cols) for i in range(rows)]

# Print dots on sheet
for dot in dotVerticies:
    sheet[dot[1]][dot[0]] = '#'

def printSheet():
    for row in range(rows):
        print(''.join(sheet[row]))

#printSheet()

answer1 = 0
# Do fold
for fold in foldInstructions:
    foldLine = fold[1]
    if fold[0] == 'y':
        foldSize = rows - foldLine

        for foldStep in reversed(range(foldSize)):
            for col in range(cols):
                source = sheet[foldLine + foldStep][col]
                target = sheet[foldLine - foldStep][col]
                if target == '#' and source == '#':
                    dotCount -= 1
                elif source == '#':
                    sheet[foldLine - foldStep][col] = '#'
            sheet.pop()
            rows -= 1

    if fold[0] == 'x':
        foldSize = cols - foldLine

        for foldStep in reversed(range(foldSize)):
            for row in range(rows):
                source = sheet[row][foldLine + foldStep]
                target = sheet[row][foldLine - foldStep]
                if target == '#' and source == '#':
                    dotCount -= 1
                elif source == '#':
                    sheet[row][foldLine - foldStep] = '#'
                sheet[row].pop()
            cols -= 1
    
    if not answer1:
        answer1 = dotCount

print("Day13, part1, answer:", answer1)
print("Day13, part2, answer:")
printSheet()