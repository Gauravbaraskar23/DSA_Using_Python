# st = []
# st.append(8) # add element at the top
# st.append(2)
# st.append(5)
# st.append(7)  
# st.append(1)

# print(st)
# print(st.pop())  # Pop last element
# print(st[-1])    # returns top element


# Implementation using List

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
    
    def displayAll(self):
        if len(self.st) == 0:
            return -1
        
        for i in range(len(self.st)):
            print(self.st[i] , end = ' ')
stk = Stack()

stk.push(5)
stk.push(8)
stk.push(4)
stk.push(9)

stk.displayAll()
print()
print(stk.pop())
print(stk.top())

print(stk.size())

stk.displayAll()



