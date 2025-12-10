# 160. Intersection of two linked list.

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


#  Intersection of two linked list.
def intersectionOfTwoList(headA , headB):
    p1 = headA
    p2 = headB
    count = 0
    while True:
        if p1 == p2:
            return p1
        
        
        p1 = p1.next 
        p2 = p2.next 
        
        if p2 == None:
            count += 1
            p2 = headA
        
        if p1 == None:
            p1 = headB
            

        if count > 1:
            return None
         
intersectionOfTwoList(head , head)

     


# Intersection of two linked list using length