# Create a list of all odd numbers between 1 and max number.
odd_list = []
max_num = int(input("Enter a number:"))
for num in range(1 , max_num):
    if num %2 != 0:
        odd_list.append(num)
print(odd_list)