import os
import statistics

inputfile = os.path.dirname(__file__) + "\\input.txt"

# Init data
crabsx = [int(x) for x in open(inputfile).read().strip().split(',')]

xalignment = int(statistics.median(crabsx))
print("Crab X Alignment: ", xalignment)

fuel = sum([abs(xalignment - x) for x in crabsx])

print("Day7, Part1 Answer: ", fuel)