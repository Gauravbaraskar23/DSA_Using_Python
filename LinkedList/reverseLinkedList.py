# 206. Reverse Linked List

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
insertAtEnd(head , 1)
insertAtEnd(head , 5)
insertAtEnd(head , 8)
insertAtEnd(head , 4)


# Reverse Linked List

def reverseLinkedList(head):
    curr = head
    prev = None
    nxt = None
    
    while curr != None:
        nxt = curr.next 
        curr.next = prev
        prev = curr
        curr = nxt
    
    while prev != None:
        print(prev.data , end = " ")   
        # prev.data , end = " "
        prev = prev.next 
        
    return prev    

reverseLinkedList(head)

# def palindrome(head , prev):
#     if head == prev:
#         return True
#     return False

# print(palindrome(head , reverseLinkedList(head)))
