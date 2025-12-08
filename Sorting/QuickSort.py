def partition(nums, l, r):
    key = nums[r]
    start = l
    for i in range(l , r+1):
        if nums[i] <= key:
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp
            start += 1
    
    return start -1

def quickSort(nums, l, r):
    if l >=r :
        return 
    
    p = partition(nums , l , r)
    
    quickSort(nums , l , p-1)
    quickSort(nums , p+1 , r)
    
def sortArr(nums):
    n = len(nums)
    quickSort(nums , 0 , n-1)
    
    return nums

print(sortArr([87,54,2,5,57,7,1]))
    