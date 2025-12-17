# Detect cycle in undirected Graph using DFS

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


adjList2 = [[1,3,4],
            [0,2,],
            [1],
            [0],
            [0]
            ]


visited = [False] * n 

def dfs(i, parent, adjList, visited):
    visited[i] =True
    
    for x in adjList[i]:
        if x == parent:
            continue
        if visited[x]:
            return True
        if dfs(x, i, adjList, visited):
            return True
    return False

print(dfs(0, -1, adjList, visited))

