# 45. Binary Search

def binarySearch(nums , target):
    n = len(nums)
    
    l = 0
    r = n -1
    
    while l <=r:
        mid = (l+r) //2
        if nums[mid] == target:
            return mid
        elif  target > nums[mid]:
            l  = mid+1
        else:
            r = mid -1
            
    return -1

print(binarySearch([-1,0,3,5,9,12], 9))