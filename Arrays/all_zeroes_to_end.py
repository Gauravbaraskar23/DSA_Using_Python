def move_zeroes_to_end(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i] , arr[count] = arr[count] , arr[i]
            count+= 1
    return arr

# n = int(input("Enter the length of array: "))
# arr =[]
 
# for i in range(n):
#     arr.append(int(input('Enter an element: ')))
arr = [1,2,0,4,3,0,5,0]
print(move_zeroes_to_end(arr))