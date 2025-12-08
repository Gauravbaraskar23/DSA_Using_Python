# 905. Sort array by parity
def sortArrByParity(nums):
    n = len(nums)
    start = 0
    if n == 1:
        return nums
    
    for i in range(n):
        if nums[i] % 2 == 0:
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp
            start +=1
    
    return nums

print(sortArrByParity([5,4,2,7,6,9]))
