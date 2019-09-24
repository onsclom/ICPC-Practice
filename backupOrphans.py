import sys

indexMode = True
indexDict = {}
fFiles = []

for line in sys.stdin:
    line = line.replace('\n','')
    if indexMode:
        if line == "":
            indexMode = False
        else:
            indexDict[line]=True

    else: #!indexMode:
        fileName = ""
        underscoreCount = 0 
        for x in range(len(line)-1, -1, -1):
            if line[x] == '_':
                underscoreCount+=1
                if underscoreCount==2:
                    fileName = line[0:x] #cuts off _ and everything after
                    break
        
        if fileName in indexDict:
            indexDict[fileName]=False
        else:
            fFiles.append(line)

#now sort all F files and output
fFiles.sort()
for f in fFiles:
    print("F " + f)

#now get all I files, sort, and output
iFiles=[]
for x in indexDict:
    if indexDict[x]==True:
        iFiles.append(x)

iFiles.sort()
for i in iFiles:
    print("I " + i)

if(len(iFiles)==0 and len(fFiles)==0):
    print("No mismatches.")




