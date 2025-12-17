# BFS is always done using Queue

# Queue
class Queue:
    def __init__(self):
        self.q = []
        self.front = -1
        
    def push(self , x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)
        
        
    def pop(self):
        if len(self.q) == 0:
            return -1
        
        x = self.q[self.front]
        self.front +=1
        
        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x
        
    def getFront(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]
    
    
    
    def size(self):
        if self.front == -1:
            return 0 
        
        return len(self.q) - self.front


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
        
q = Queue()
visited = [False] * n 
ans = []  # for storing BFS traversal

q.push(0)
visited[0] = True
ans.append(0)

while q.size() > 0:
    front = q.pop()
    for x in adjList[front]:
        if not visited[x]:
            q.push(x)
            visited[x] = True
            ans.append(x)
print(ans)

 

