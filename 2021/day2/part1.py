input = open("day2\\input.txt", "r")

pos = 0
depth = 0

while True:
    line = input.readline().replace("\n", "")
    if not line:
        break

    vector = line.split(" ")
    direction = vector[0]
    magnitude = int(vector[1])

    if direction == "forward":
        pos += magnitude
    elif direction == "down":
        depth += magnitude
    elif direction == "up":
        depth -= magnitude

input.close()
print("Day2, Part1 answer: " + str(pos*depth))