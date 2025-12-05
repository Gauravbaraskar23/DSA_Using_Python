# 1. Two Sum
def twoSum(numms, target):
    n = len(nums)
    dict1 = {}
    for i in range(n):
        rem = target - nums[i]
        
        if rem in dict1:
            return [dict1[rem], i]

        dict1[nums[i]] = i
        
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
        
        