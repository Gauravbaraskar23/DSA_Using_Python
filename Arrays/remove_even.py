#Write a Python program to print the numbers of a specified list after removing even numbers from it.

numbers = [1,2,3,5,6,7,8]
       
numbers = [x for x in numbers if x%2 != 0 ]
print(numbers)