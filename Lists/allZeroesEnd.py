def allZeroesEnd(nums):
    n = len(nums)
    count = 0
    
    for i in range(n):
        if nums[i] != 0:
            temp = nums[i]
            nums[i] = nums[count]
            nums[count] = temp
            count +=1
        
        
    return nums

print(allZeroesEnd([2,0,6,5,0,0,5,5,0,8,47,0,8548,48]))
    