def sortArr(nums):
    n = len(nums)
    
    for i in range(n):
        mn = nums[i]
        ind = i
        for j in range(i+1 , n):
            if nums[j] < mn:
                mn = nums[j]
                ind = j
        
        temp = nums[i]
        nums[i] = nums[ind]
        nums[ind] = temp

    
    return nums
print(sortArr([87,45,488,77,5]))
        