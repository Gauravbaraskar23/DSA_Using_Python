# Depth First Search using recursion



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

# for i in range(n):
#     print(i, "-->", adjList[i])
 


visited = [False] * n 
ans = []  # for storing BFS traversal

# st.push(0)
# visited[0] = True
def dfs(i, adjList, visited):
    visited[i] =True
    ans.append(i)
    
    for x in adjList[i]:
        if not visited[x]:
            dfs(x, adjList, visited)
dfs(0, adjList, visited)
print(ans)