# 35. Search Insert Position

def lowerBound(nums , target):
    n = len(nums)

    l = 0
    r = n-1
    ans= n
    
    while l <= r:
        mid = (l+r) //2
        if nums[mid] >= target:
            ans = mid
            # Left side     
            r = mid-1
            
        else:
            # Right side
            l = mid+1
    
    return ans  

      
def searchInsert(nums , target):
    return lowerBound(nums, target)

print(searchInsert([1,2,3,4,6] , 5))