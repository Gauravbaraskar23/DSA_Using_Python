
# #For largest Number
# lst = [1,34,6,74,3,84,4]
# max_num = lst[0]
# for i in range(1,len(lst)):
#     if lst[i] > max_num:
#         max_num = lst[i]
# print("Largest number is:",max_num)
        
# #For Minimum number
# min_num = lst[0]
# for i in range(1,len(lst)):
#     if lst[i] < min_num:
#         min_num = lst[i]
# print("Smallest number is:",min_num)



def largestNumber(nums):
    n = len(nums)
    max_num = 0
    for i in range(n):
        if nums[i] > nums[max_num]:
            nums[max_num] = nums[i]
            
    return nums[max_num]

print(largestNumber([56,4,5,6,4,8,778,111,5,55,4]))