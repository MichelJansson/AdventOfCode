input = open("day2\\input.txt", "r")

aim = 0
pos = 0
depth = 0

while True:
    line = input.readline().replace("\n", "")
    if not line:
        break

    commandArr = line.split(" ")
    command = commandArr[0]
    value = int(commandArr[1])

    if command == "forward":
        pos += value
        depth += (aim * value)
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value

input.close()
print("Day2, Part2 answer: " + str(pos*depth))