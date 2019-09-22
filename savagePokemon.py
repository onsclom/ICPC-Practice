class graphNode:
    def __init__(self):
        self.inList = []
        self.outList = []

def pokemonCheck(graph):
    #do DFS on 0 to see
    canSeeAll = [False] * len(graph)
    visited = [False] * len(graph)

    currentIndex = 0
    visited[0] = True
    DFSstack = []

    for x in graph[currentIndex].outList:
        if visited[x]==False and x!=currentIndex:
            DFSstack.append(x)
            visited[x] = True

    while (len(DFSstack)!=0):
        currentIndex = DFSstack.pop(0)
        
        for x in graph[currentIndex].outList:
            if visited[x]==False and x!=currentIndex:
                DFSstack.append(x)
                visited[x] = True

    for x in visited:
        if x==False:
            return False

    #if still here then it passed the first DFS
    #0 can see all

    visited = [False] * len(graph)
    currentIndex = 0
    
    #now to see if all can see 0

    for x in graph[currentIndex].inList:
        if visited[x]==False and x!=currentIndex:
            DFSstack.append(x)
            visited[x] = True

    while (len(DFSstack)!=0):
        currentIndex = DFSstack.pop(0)
        
        for x in graph[currentIndex].inList:
            if visited[x]==False and x!=currentIndex:
                DFSstack.append(x)
                visited[x] = True

    for x in visited:
        if x==False:
            return False

    #if still, then everything goes into 0 somehow
    #therefore return true

    return True


amount = input()

for x in range(int(amount)):
    nodes, edges = input().split()

    #initialize list of nodes
    graph = [graphNode() for j in range(int(nodes))]
    for i in range(int(edges)):

        #each thing is a connection from node1 -> node2

        eStart, eEnd = input().split()
        eStart = int(eStart)
        eEnd = int(eEnd)

        graph[eEnd].inList.append(eStart)
        graph[eStart].outList.append(eEnd)

    if pokemonCheck(graph):
        print("Gotta Catch Them All!")
    else:
        print("Oh, oh!")


    
    

    

    

    





