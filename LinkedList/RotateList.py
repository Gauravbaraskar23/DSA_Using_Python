# 61. Rotate List

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
insertAtEnd(head , 4)
insertAtEnd(head , 5)
insertAtEnd(head , 6)
insertAtEnd(head , 7)


# Rotate List

def rotateList(head , k ):
    if head == None or head.next == None:
        return head
    
    
    last = head
    l = 0
    while last.next != None:
        last = last.next 
        l += 1
    l +=1
    
    k = k % l
    
    if k == 0:
        return head
    
    curr = head
    for i in range(l-k-1):
        curr = curr.next 
    
    last.next = head
    head = curr.next 
    curr.next = None
    
    
    return head

rotateList(head , 3)

traverse(head)


# Rotate List using reverse linked list
