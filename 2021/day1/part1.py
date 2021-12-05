
input = open("day1\\input.txt", "r")

prevnum = None
counter = 0

while True:
    line = input.readline().replace("\n", "")
    if not line:
        break

    num = int(line)

    if (prevnum != None and num > prevnum):
        counter += 1

    prevnum = num

input.close()
print("Day1, Part1 answer: " + str(counter))
