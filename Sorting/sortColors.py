# LeetCode Problem 75: Sort Colors
# usig two pointers approach
def sortColors(nums):
    left = 0
    right = len(nums)-1
    i =0
    
    while i <= right:
        if nums[i] == 1:
            i += 1
        elif nums[i] == 0:
            temp = nums[i]
            nums[i] = nums[left]
            nums[left] = temp
            left += 1
            i +=1 
        
        else:
            temp = nums[i]
            nums[i] = nums[right]
            nums[right] = temp
            right -= 1
            i +=1 
    return nums       
print(sortColors([2,0,2,1,1,0]))   