# 852. Peak Index in a Mountain Array

def peakIndexInMountainArray(nums):
    n = len(nums)
    l = 0 
    r = n-2
    
    ans  = n-1
    
    while l<= r:
        mid = (l+r) // 2
        if nums[mid] < nums[mid+1]:
            l = mid +1  # Right side
            
        else:
            ans= mid
            r = mid - 1 #  for Left side
            
    return ans 
    
print(peakIndexInMountainArray([0,1,2,6,4,2,1]))