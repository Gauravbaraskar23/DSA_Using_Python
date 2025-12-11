# 496. Next Greater element-I

def nextGreaterEle(nums1 , nums2):
    n = len(nums2)
    
    ans = {}
    st = []
    
    for i in range(n-1 ,-1,-1):
        while len(st) >0 and st[-1] <= nums2[i]:
            st.pop()
            
        if len(st) == 0:
            ans[nums2[i]] = -1
        
        else:
            ans[nums2[i]] = st[-1]
            
        st.append(nums2[i])
        
        
    return list(map(lambda x: ans[x] , nums1))
    # OR   
    # res = []
    # for i in nums1:
    #     res.append(ans[i])
        
    # return res
    
arr1 = [4,1,2]
arr2 = [1,3,4,2]
print(nextGreaterEle(arr1 , arr2))