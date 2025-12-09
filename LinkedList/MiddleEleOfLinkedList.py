# 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None 
        
            
a = Node(5)
b = Node(3)
c  = Node(7)

head = a
head.next = b
head.next.next = c  


def insertAtKthPosition(head , data , k):
    newNode = Node(data)
    
    curr = head
    for i in range(k-1):
        curr = curr.next
    
    newNode.next = curr.next
    curr.next = newNode
    
    return head

insertAtKthPosition(head , 15 , 2)

# Finding middle element of linked list
"""def middle(head):
    curr  = head
    length = 0
    
    while curr != None:
        curr= curr.next 
        length +=1
    
    curr = head    
    for i in range(length// 2):
        curr = curr.next 
        
    return curr
print(middle(head).data)
# """


#  Using fast and slow pointer approach
def middleNode(head):
    slow= head
    fast = head 
    
    while fast != None and fast.next != None:
        slow = slow.next 
        fast = fast.next.next 
        
    return slow

print(middleNode(head).data)