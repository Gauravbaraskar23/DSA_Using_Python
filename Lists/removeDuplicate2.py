# 80 Remove duplicate from sorted array and print same elements at most 2 times.
nums = [3,3,5,7,7,7,7,9,9,9,12,12]
n = len(nums)
start = 1

if n<= 2:
    print(n)
    
    
for i in range(1,n):
    if nums[i] != nums[start-1]:
        start += 1
        nums[start] = nums[i] 
    
print(f"Same elements at most 2 times: {start+1}")
print(nums)


