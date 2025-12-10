# Queue Implementation using Linked List

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        
    def push(self,x):
        self.length += 1
        newNode = Node(x)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
            
        else:
            self.rear.next = newNode
            self.rear = newNode      
            
    def pop(self):
        if self.front is None:
            return -1
        
        x = self.front.data
        self.front = self.front.next
        self.length -= 1
        
        if self.front is None:
            self.rear = None
        
        return x
    
    def getFront(self):
        if self.front is None:
            return -1
        
        return self.front.data
    
    def size(self):
        return self.length
    
   
que = Queue()

que.push(5)
que.push(8)
que.push(4)
que.push(9)

print(que.getFront())

print(que.pop())
print(que.getFront())

print(que.size())



    
            
            

        
