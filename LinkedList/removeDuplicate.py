# 83. Remove Duplicates from an sorted Linked List



class Node:
    def __init__(self , data):
        self.data = data
        self.next = None 
        
            
a = Node(4)
b = Node(4)
c  = Node(5)

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
insertAtEnd(head , 9)
insertAtEnd(head , 10)
insertAtEnd(head , 10)



# Remove Duplicates
def removeDuplicates(head):
    curr = head
    if head == None or head.next == None:
        return head
    
    while curr != None and curr.next != None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next 
        else:
            curr = curr.next 
            
    return head

removeDuplicates(head)
traverse(head)