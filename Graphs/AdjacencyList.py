# Adjacency List 

n = 6  # No. of vertices/Nodes
e = 7 # No. of Edges

edges = [(0,1), (0,3), (0,4), (1,2), (1,5) , (2,4), (3, 4)]


adjList = []
for i in range(n):
    adjList.append([])
    
for edge in edges:
    x = edge[0]
    y = edge[1]
    
    adjList[x].append(y)
    adjList[y].append(x)

for i in range(n):
    print(i, "-->", adjList[i])
    