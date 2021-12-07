import os
import math

inputfile = os.path.dirname(__file__) + "\\input.txt"

# Init data
crabsx = [int(x) for x in open(inputfile).readline().strip().split(',')]

leastFuel = math.inf
for xalignment in range(min(crabsx), max(crabsx)):
    fuel = 0
    for x in crabsx:
        steps = abs(xalignment - x)
        fuel += (steps * (steps + 1)) / 2
    if fuel < leastFuel:
        leastFuel = fuel

print("Crab X Alignment: ", xalignment)

answer = int(leastFuel)
print("Day7, Part2 Answer:", answer)