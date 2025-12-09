class Node:
    def __init__(self , data):
        self.data = data
        self.next = None 
        
    def traverse(self):
        current = head
        
        while current != None:
            print(current.data , end = " ")
            current = current.next
            
a = Node(5)
b = Node(3)
c  = Node(7)

head = a
head.next = b
head.next.next = c


# Traversig the linked list
def traverse(head):
    current = head
        
    while current != None:
        print(current.data , end = " ")
        current = current.next
# traverse(head)

# Insertion at the beginning
def insertAtStart(head , data):
    newNode= Node(data)
    newNode.next = head
    head = newNode
    return head

head = insertAtStart(head , 10)
# traverse(head)


# Insertion at the end
def insertAtEnd(head , data):
    newNode = Node(data)
    
    
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = newNode
    
    return curr.next
insertAtEnd(head , 1)
# traverse(head)

# insertion at a kth index position

def insertAtKthPosition(head , data , k):
    newNode = Node(data)
    
    curr = head
    for i in range(k-1):
        curr = curr.next
    
    newNode.next = curr.next
    curr.next = newNode
    
    return head

insertAtKthPosition(head , 15 , 2)

# traverse(head)

# Deletion at the beginning

# def deleteAtStart(head):
#     head = head.next
#     return head
    

# deleteAtStart(head)
# # print()
head  = head.next

# traverse(head)
  
# Deletion at the end
def deleteAtEnd(head):
    curr = head
    while curr.next.next != None:
        curr = curr.next
    
    curr.next = None    
    
deleteAtEnd(head)
# traverse(head)

# Deletion at kth position
def deleteAtKthPosition(head , k):
    curr = head
    
    for i  in range(k-1):
        curr = curr.next
    
    curr.next = curr.next.next
    
deleteAtKthPosition(head , 2)
traverse(head)
    
    
