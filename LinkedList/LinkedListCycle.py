# 141. Linked List Cycle

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


# Detect cycle exist or not.
def hasCycle(head):
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next 
        fast = fast.next 
        
        if slow == fast:
            return True
    return False

print(hasCycle(head))
         