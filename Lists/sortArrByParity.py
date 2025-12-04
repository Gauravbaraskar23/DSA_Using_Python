# 905. Sort array by parity

nums = [3,1,2,4]
n = len(nums)
start = 0
if n <= 1:
    print(nums)
    
    
for i in range(n):
    if nums[i] % 2 == 0:
        temp = nums[i]
        nums[i] = nums[start]
        nums[start] = temp
        start += 1
  
print(f"Sort array based on the parity : {nums}")
