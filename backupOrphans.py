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
        for x in range(len(line)):
            if line[x] == '_':
                fileName = line[0:x-len(line)] #cuts off everything after _
                print(fileName)
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





