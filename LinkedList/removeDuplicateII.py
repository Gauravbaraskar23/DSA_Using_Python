# 82. Remove Duplicates from Sorted List II

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None 
        
            
a = Node(1)
b = Node(2)
c  = Node(3)

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
insertAtEnd(head , 3)
insertAtEnd(head , 4)
insertAtEnd(head , 5)
insertAtEnd(head , 5)


# Remove Duplicates from Sorted List II
def removeDulicate(head):
    curr = head
    dummy = Node(0)
    prev = dummy    
    while curr:
        # Check for duplicates
        if curr.next and curr.data == curr.next.data:
            # Skip all nodes with the same value
            while curr.next and curr.data == curr.next.data:
                curr = curr.next
            # Move to the next distinct element
            curr = curr.next
        else:
            # No duplicates, link the node to the new list
            prev.next = curr
            prev = prev.next
            curr = curr.next
        
    prev.next = None  # Terminate the list
    return dummy.next

removeDulicate(head)
traverse(head)