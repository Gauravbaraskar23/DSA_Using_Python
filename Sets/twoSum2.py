# 167. Two Sum II - Input Array Is Sorted, return indces starting from 1.

def twoSum(nums , target):
    left = 0 
    right = len(nums) - 1
    
    while left < right:
        sum1 = nums[left] + nums[right]

        if sum1 == target:
            return [left +1, right + 1]
        
        elif sum1 > target:
            right -= 1
        
        else:
            left +=1
            
nums = [2,3,4]
target = 6

print(twoSum(nums , target))