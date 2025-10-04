def second_largest(arr):
    n = len(arr)
    largest = -1
    second_largest =-1
    
    for i in range(n):
        if arr[i] > largest:
            second_largest  = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]
    
    return second_largest    

arr = [22,3,4,56,7,21]
print(second_largest(arr))