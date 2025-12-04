# 53. Give an array nums,find the subarray with the largest sum and return its sum.
# Kadanes's Algorithm : for finding maximumm subarray

nums = [5,-1,-7,6,2,-3,5,-10,2]

curr_sum = 0
max_sum = nums[0]

for i in range(len(nums)):
    curr_sum += nums[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
    
    if curr_sum < 0:
        curr_sum  = 0

print(max_sum)
