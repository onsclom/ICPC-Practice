import sys

for line in sys.stdin:
    curNum = int(line)
    print(str(curNum) + ":")
    for x in range(2, int((curNum/2)+2)):
        y=int(x-1)
            #see if curNum % x+y == 0 OR curNum % x+y == x
        if curNum % x+y == 0 or curNum % x+y == x:
            print(" " + str(x) + "," + str(y))    
        y=int(x)
        if curNum % x+y == 0 or curNum % x+y == x:
            print(" " + str(x) + "," + str(y))    
            
exit(0)