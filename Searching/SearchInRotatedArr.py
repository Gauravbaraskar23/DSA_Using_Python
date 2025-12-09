# 33. Search in rotated sorted array

def search(nums, target):
    
    n = len(nums)
    l = 0
    r = n-1
    ans =n-1
    
    while l <=r:
        mid = (l+r) // 2
        # if nums[l] != target:
        #     return -1
        
        if nums[mid] == target:
           return mid
       
        
        if nums[l] <= nums[mid]:
             if nums[l] <= target < nums[mid]:
                r = mid -1
             else:
                l = mid +1
            
        else:
            if nums[mid] < target <= nums[r]:
                l = mid+1
            else:
                r = mid-1
            
    
    return -1
    
print(search([4,5,6,7,0,1,2], 0)) 