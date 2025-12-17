# Depth First Search

# we use Stack for DFS

class Stack:
    def __init__(self):
        self.st = []
        
    def push(self , x):
        self.st.append(x)
        
    def pop(self):
        if len(self.st) == 0:
            return -1
        
        x = self.st[-1]
        self.st.pop()
        return x
        
    def top(self):
        if len(self.st) == 0:
            return -1
        return self.st[-1]
    
    
    def size(self):
        return len(self.st)
    


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
 

st = Stack()
visited = [False] * n 
ans = []  # for storing BFS traversal

st.push(0)
visited[0] = True
# ans.append(0)

while st.size() > 0:
    top = st.pop()
    ans.append(top)
    for x in adjList[top]:
        if not visited[x]:
            st.push(x)
            visited[x] = True
print(ans)

 

