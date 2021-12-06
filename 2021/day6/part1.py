import os

inputfile = os.path.dirname(__file__) + "\\input.txt"

# Init data
fishes = [int(x) for x in open(inputfile).readline().strip().split(',')]

for dayi in range(80):
    fishcount = len(fishes)
    for fishi in range(fishcount):
        if fishes[fishi] == 0:
            fishes[fishi] = 6
            fishes.append(8)
        else:
            fishes[fishi] -= 1

    #print("Day", dayi, fishes)


answer = len(fishes)
print("Day6, Part1 Answer: ", answer)
