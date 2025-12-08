def sortArray(nums):
    n = len(nums)
    
    for i in range(n):
        isSwap  = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                isSwap =True
        
        if not isSwap:
            break
                
    return nums

print(sortArray([3,2,8,1,7,6,4]))
    
