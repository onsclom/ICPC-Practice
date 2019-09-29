#Manual Cipher
import sys

def cipherSelect(counter, iterations):
    highest = iterations[len(iterations)-1]
    answer = 0
    for x in iterations:
        if counter >= x:
            answer += 1
    return answer

firstLine = input()
firstLine.replace('\n', '')
parts = firstLine.split(':')

#parts[0]=BLUE
#parts[1]=2314  ... sum these all up.. 10, then 5, 6, 10... remainder can be compared to these to know where at

chars = ['A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
charsDict = {
'A' : 0,
'B' : 1,
'C' : 2,
'D' : 3,
'E' : 4,
'F' : 5,
'G' : 6,
'H' : 7,
'I' : 8,
'J' : 9,
'K' : 10,
'L' : 11,
'M' : 12,
'N' : 13,
'O' : 14,
'P' : 15,
'Q' : 16,
'R' : 17,
'S' : 18,
'T' : 19,
'U' : 20,
'V' : 21,
'W' : 22,
'X' : 23,
'Y' : 24,
'Z' : 25,
' ' : 26
}

iterations = list(parts[1])
runningSum = 0
for x in range(len(iterations)):
    curX = int(iterations[x])
    runningSum += curX
    iterations[x] = runningSum


keys = []

for x in range(len(parts[0])):
    cur = parts[0][x]
    count = 0
    for x in range(len(chars)):
        if chars[x] == cur:
            break
        count += 1
    keys.append(count)


#KEYS ARE WHERE TO START!!! booyah

for line in sys.stdin:
    count = 0
    line = line.replace('\n', '')
    line = list(line)

    for x in range(len(line)):
        #editing to new chars
        current = charsDict[line[x]]

        current -= keys[cipherSelect(count,iterations)]

        current = current % 27

        line[x] = chars[current]

        count += 1
        if count >= iterations[len(iterations)-1]:
            count = 0

    output = ""
    for y in line:
        output += str(y)

    print(output.lower())

