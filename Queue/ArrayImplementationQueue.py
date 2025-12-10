# Queue Implementation using queue 


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
    
    
        
    
que = Queue()

que.push(5)
que.push(8)
que.push(4)
que.push(9)

print(que.getFront())

print(que.pop())
print(que.getFront())

print(que.size())




