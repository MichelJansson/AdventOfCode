import os

inputfile = os.path.dirname(__file__) + "\\input.txt"

# Init data
lines = [x.strip() for x in open(inputfile).readlines()]

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
syntaxErrorPoints = [3, 57, 1197, 25137]
autocompletePoints = { '(':1, '[':2, '{':3, '<':4}

syntaxErrorScore = 0
autocompleteScores = []
for line in lines:
    queue = []
    for char in line:
        if char in opening:
            queue.append(char)
        elif char in closing:
            charIndex = closing.index(char)
            if opening[charIndex] != queue.pop():
                print("Illegal char found:", char)
                syntaxErrorScore += syntaxErrorPoints[charIndex]
                queue.clear()
                break # stop caring
    
    if len(queue) > 0:
        autocompleteScore = 0
        for remaining in reversed(queue):
            autocompleteScore = autocompleteScore * 5 + autocompletePoints[remaining]
        print("Inclomplete line score:", autocompleteScore)
        autocompleteScores.append(autocompleteScore)

answer1 = syntaxErrorScore
answer2 = sorted(autocompleteScores)[len(autocompleteScores)//2]

print("Day10, part1, answer:", answer1)
print("Day10, part2, answer:", answer2)