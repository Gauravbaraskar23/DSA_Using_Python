# 2. Add two numbers

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None 
        
            
a = Node(2)
b = Node(9)
c  = Node(4)

head = a
head.next = b
head.next.next = c  

d = Node(5)
e = Node(2)
f = Node(0)
head1 = d
head1.next = e
head1.next.next = f

# Traversig the linked list
def traverse(head):
    current = head
        
    while current != None:
        print(current.data , end = " ")
        current = current.next

# Traversig the linked list head1
def traverse1(head1):
    current = head1
        
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
# insertAtEnd(head , 9)
# insertAtEnd(head , 3)
# insertAtEnd(head , 8)
insertAtEnd(head , 5)


# add two numbers

# def addTwoNumbers(head1 , head2):
    # curr1 = head1
    # curr2 = head2
    
    # l1 = 0
    # l2 = 0
    
    # while curr1 != None:
    #     curr1 = curr1.next 
    #     l1 +=1
        
    # while curr2 != None:
    #     curr2 = curr2.next 
    #     l2 += 1 
        
# add two numbers

def addTwoNumbers(head1 , head2):
    curr1 = head1
    curr2 = head2
    
    ans =Node(-1)
    c= 0
    curr3 = ans
    
    while curr1 != None or curr2 != None:
        total = c
        c = 0
        if curr1 != None:
            total += curr1.data
            curr1 = curr1.next 
             
        if curr2 != None:
            total += curr2.data
            curr2 = curr2.next 
        
        if total > 9:
            c = 1
            total -=10
            
        newNode = Node(total)
        curr3.next = newNode
        curr3 = curr3.next 
        
    if c >0:
        newNode = Node(c)
        curr3.next = newNode
    
    # while curr3 != None:
    #     print(curr3.data, end= " ")
    #     curr3 = curr3.next 
        
    return ans.next

addTwoNumbers(head , head1)    
# print(addTwoNumbers(head , head1) )            
    