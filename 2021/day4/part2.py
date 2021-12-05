input = open("day4\\input.txt", "r")

numbers = None
boards = []

# Init data (as strings)
for rawline in input.readlines():
    line = rawline.rstrip()

    # First row
    if not numbers: 
        numbers = line.split(',')
        continue
    
    # Empty row = new board is about to begin
    if line == '':
        boards.append([])
        continue

    boards[-1].append(line.split())

input.close()

winningnumber = None
#winningboard = None
winningboards = {}

# Lets play BINGO!
for number in numbers:

    for boardindex in range(len(boards)):
        if boardindex in winningboards:
            continue

        board = boards[boardindex]

        # mark and check line
        for line in board:
            winline = True
            for colnum in range(len(line)):
                if line[colnum] == number:
                    line[colnum] = "x"
                if line[colnum] != 'x':
                    winline = False

            if winline: break

        # check cols
        for colnum in range(len(board[0])):
            wincol = True
            for linenum in range(len(board)):
                if board[linenum][colnum] != 'x':
                    wincol = False
                    break

            #winning col!
            if wincol: break

        #winning board!
        if winline or wincol:
            winningnumber = number
            winningboards[boards.index(board)] = board
            #break

    #if winningnumber: break

winningboard = winningboards.popitem()[1]

print("Last Winning board:")
for line in winningboard:
    print(line)

print("Last Winning number:" + winningnumber)

# add all non marked numbers
nonmarked = 0
for line in winningboard:
    for linecol in line:
        if linecol.isdigit():
            nonmarked += int(linecol)

print("Non marked: " + str(nonmarked))
print("Day4, Part2 Final score: " + str(int(winningnumber) * nonmarked))