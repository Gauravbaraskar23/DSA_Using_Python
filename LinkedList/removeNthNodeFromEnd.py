# 19. Remove Nth Node From End of Linked List
# Given the head of a linked list, remove the nth node from the end of the list


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

# Deletion nth node from end
def deleteAtKthPosition(head , n):
    p1 = head
    p2 = head 
    
    for i in range(n):
        p2 = p2.next 
        
    if p2 == None:
        head =  head.next
        return head
    
    while p2.next != None:
        p1 = p1.next 
        p2 = p2.next 
    
    p1.next = p1.next.next 
    
    
    return head

            
    
        
traverse(head)
print()
deleteAtKthPosition(head ,6)
traverse(head)