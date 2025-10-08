import heapq
li = [12,3,4,5,54,23]
heapq.heapify(li)

print("Heap queue: " , li)  #By default min heap created

# For creating max heap by inverting values
max_heap = [-n for n in li]
heapq.heapify(max_heap)

# Access largest element(invert sign again)
print("Largest Element :" , -max_heap[0])

#Appending an element
heapq.heappush(li ,6 )

print(li)  # Before popping

min = heapq.heappop(li)  # Pop the smallest element
print("Smallest :" , min)
print(li)

# Appending and popping simultaneously
print("Appending and popping simultaneously")
min = heapq.heappushpop(li , 11)
print("\nPop the smallest element from the list:" ,min)

print("New list is:" , li)

# Finding largest & smalllest element
'''
1. heapq.nlargest(n, iterable) returns the n largest elements from the iterable.
2. heapq.nsmallest(n, iterable) returns the n smallest elements from the iterable.
'''

maxi = heapq.nlargest(3 , li)   # here 3 largest element printed.
print("3 largest elements:" , maxi)

mini = heapq.nsmallest(3 , li)
print("3 smallest element:",mini)


# Replace and merge operations

replace_ele = heapq.heapreplace(li , 34) # replacing smallest element with 34
print(replace_ele)
print(li)

# merging
l2 = [2,4,6,7,8]


l3 = list(heapq.merge(li , l2))

print("After merging li and l2 :" , l3)

