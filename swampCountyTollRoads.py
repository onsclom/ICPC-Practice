import sys

curLine = input()
dict = {}

while (curLine != ""):
    parts = curLine.split(" ")
    dict[parts[0]]=parts[1]

    curLine = input()


for line in sys.stdin:
    res = 1
    for x in line:
        if x in dict:
            res *= float(dict[x])
    print('%.3f' % res)

exit(0)