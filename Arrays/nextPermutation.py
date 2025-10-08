'''
Company Tags
Infosys, Flipkart, Amazon, Microsoft, FactSet , Hike, MakeMyTrip, Google, Qualcomm,Salesforce
'''
class Solution:
    
    def nextPermutation(self , arr):
        n = len(arr)
        
        #Find first decreasing element from right
        i = n-2
        while i>=0 and arr[i]>= arr[i+1]:
            
            i-= 1
        # if found , find next greater element to swap
        if i>=0:
            j = n-1
            while arr[j] <= arr[i]:
                j-= 1
            arr[i] , arr[j] = arr[j]  , arr[i]
            
        # # Reverse the part after i
        arr[i+1:] = reversed(arr[i+1:])
        
        return arr

arr = [2,4,1,7,5,0]       
sol = Solution()
print(sol.nextPermutation(arr))