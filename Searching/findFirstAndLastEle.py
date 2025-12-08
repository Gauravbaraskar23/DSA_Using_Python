# 34. Find first and last position of element in sorted array

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

def upperBound(nums , target):
    n = len(nums)

    l = 0
    r = n-1
    ans= n
    
    while l <= r:
        mid = (l+r) //2
        if nums[mid] > target:
            ans = mid
            # Left side     
            r = mid-1
            
        else:
            # Right side
            l = mid+1
    
    return ans  

def searchRange(nums, target):
    lb = lowerBound(nums,target)
    ub = upperBound(nums,target)
    
    if lb == ub :
        # not present
        return [-1,-1]
    
    else:
        return [lb , ub -1]
    
print(searchRange([5,7,7,8,8,8,10], 8))