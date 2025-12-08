# Problem NO. 88: Merge Sorted Array
def mergeSortArr(nums1, nums2, m,n):
    
    i = m-1
    j = n-1
    k = m+n -1
    
    while j >= 0:
        if nums2[j] > nums1[i] and i >=0:
            nums1[k] = nums2[j]
            j -=1 
            k -=1
        
        else:
            nums1[k] = nums1[i]
            k -=1
            i -=1
    return nums1

print(mergeSortArr([1,2,3,0,0,0], [2,5,6], 3,3))