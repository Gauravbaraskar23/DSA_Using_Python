# 26 Remove duplicate from sorted array and print unique elements
nums = [3,3,5,7,7,7,7,9,9,9,12,12]
n = len(nums)
start = 0
for i in range(1,n):
    if nums[i] != nums[start]:
        start += 1
        nums[start] = nums[i] 
    
    

print(f"Unique numbers are : {start+1}")