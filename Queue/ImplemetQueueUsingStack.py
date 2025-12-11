# 232. Implement queue using stack

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self , x):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
            
    
    def pop(self):
       x = self.stack1[-1]
       self.stack1.pop()
       return x 
        
    def peek(self):
        return self.stack1[-1]
    
    
    def empty(self):
        return len(self.stack1) == 0
    
que = MyQueue()

que.push(9)
que.push(10)

print(que.empty())
print(que.peek())
print(que.pop())
print(que.peek())

