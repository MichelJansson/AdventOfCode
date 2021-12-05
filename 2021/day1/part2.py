
input = open("day1\\input.txt", "r")

increasedcount = 0

acount = 0
asum = 0

bcount = 0
bsum = 0

ccount = 0
csum = 0

prevsum = None

linenum = 0

while True:
    line = input.readline().replace("\n", "")
    if not line:
        break
    linenum += 1
    num = int(line)

    if acount < 3:
        asum += num
        acount += 1

    if bcount < 3 and linenum > 1:
        bsum += num
        bcount += 1

    if ccount < 3 and linenum > 2:
        csum += num
        ccount += 1


    if acount == 3:
        if prevsum != None and asum > prevsum:
            increasedcount += 1
        prevsum = asum
        acount = 0
        asum = 0

    if bcount == 3:
        if prevsum != None and bsum > prevsum:
            increasedcount += 1
        prevsum = bsum
        bcount = 0
        bsum = 0

    if ccount == 3:
        if prevsum != None and csum > prevsum:
            increasedcount += 1
        prevsum = csum
        ccount = 0
        csum = 0



input.close()
print("Day1, Part2 answer: " + str(increasedcount))

