# 237. Delete Node in a Linked List
# Write a function to delete a node (except the tail) in a singly linked list,

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

# Delete a node given only access to that node
def deleteNode(node):
    node.data = node.next.data
    node.next = node.next.next
    
    return head

deleteNode(c)

traverse(head)