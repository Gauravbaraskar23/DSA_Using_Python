# 142. Linked List Cycle -II


class Node:
    def __init__(self , data):
        self.data = data
        self.next = None 
        
            
a = Node(4)
b = Node(5)
c  = Node(1)

head = a
head.next = b
head.next.next = c  

# Traversig the linked list
def traverse(head):
    current = head
        
    while current != None:
        print(current.data , end = " ")
        current = current.next
        
# insertAtEnd 
def insertAtEnd(head , data):
    newNode = Node(data)
    
    
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = newNode
    
    return curr.next
insertAtEnd(head , 9)
insertAtEnd(head , 3)
insertAtEnd(head , 8)
insertAtEnd(head , 4)


# Linked List Cycle -II

def detectCycle(head):
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next 
        fast = fast.next 
        
        hasCycle = False
        if slow == fast:
            hasCycle  = True
            break
        
    if not hasCycle:
        return None

    l = 0
    while slow.next != fast:
        slow = slow.next 
        l+= 1
    l += 1
    
    slow = slow.next 
    
    slow = head 
    fast = head
    
    for i in range(l):
        fast = fast.next 
        
    while slow != fast:
        slow = slow.next 
        fast = fast.next 
        
    return slow

print(detectCycle(head))
