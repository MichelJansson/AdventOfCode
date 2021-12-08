import os

inputfile = os.path.dirname(__file__) + "\\input.txt"

def sortChars(word):
    word = [char for char in word]
    word.sort()
    return ''.join(word)
def setDiff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

totoutput = 0
for line in open(inputfile):
    signalpattern, digitoutput = line.strip().split('|')
    signalpattern = sorted(signalpattern.strip().split(), key=len) #[2, 3, 4, 5, 5, 5, 6, 6, 6, 7]
    digitoutput = digitoutput.strip().split()

    # Map scrabled combination of segments to digit
    scrambledDigitMap = {}
    scrambled1 = ''
    scrambled4 = ''
    for signal in signalpattern:
        signal = sortChars(signal) # sort to be able to use for compare

        if len(signal) == 2:
            scrambledDigitMap[signal] = '1'
            scrambled1 = signal
        elif len(signal) == 3:
            scrambledDigitMap[signal] = '7'
        elif len(signal) == 4:
            scrambledDigitMap[signal] = '4'
            scrambled4 = signal
        elif len(signal) == 5: 
            # 2 or 3 or 5
            if all(elem in signal for elem in scrambled1): # contains a 1
                scrambledDigitMap[signal] = '3'
            elif all(elem in signal for elem in setDiff(scrambled4, scrambled1)): # contains a 4-1
                scrambledDigitMap[signal] = '5'
            else:
                scrambledDigitMap[signal] = '2'
        elif len(signal) == 6:
            # 0 or 6 or 9
            if all(elem in signal for elem in scrambled4): # contains a 4
                scrambledDigitMap[signal] = '9'
            elif all(elem in signal for elem in scrambled1): # contains a 1
                scrambledDigitMap[signal] = '0'
            else:
                scrambledDigitMap[signal] = '6'
        elif len(signal) == 7:
            scrambledDigitMap[signal] = '8'
    
    # Unscramble the output digits using the map
    digits = ''
    for scrableddigit in digitoutput:
        digits += scrambledDigitMap[sortChars(scrableddigit)]

    print(signalpattern, digitoutput, "=", digits)
    totoutput += int(digits)

answer = totoutput
print("Day8, Part2 Answer:", answer)
