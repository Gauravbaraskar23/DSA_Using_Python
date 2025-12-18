

n = 6
edges = [[0,1,4],
         [0,2,4],
         [1,2,2],
         [2,3,3],
         [2,4,1],
         [2,5,6],
         [3,5,2],
         [4,5,3]] 

adjList = []
for i in range(n):
    adjList.append([])

for edge in edges:
    x = edge[0] 
    y = edge[1] 
    w = edge[2]
    
    adjList[x].append([y,w])
    adjList[y].append([x,w])

for i in range(n):
    print(i, "-> ", adjList[i])