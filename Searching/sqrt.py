# 69. sqrt(x)

def mySqrt(num):
    if num == 0:
        return 0
    
    # l = 0
    l =1
    r = num
    
    ans = 1
    
    while l <= r:
        mid = (l+r)//2
        midSquare = mid * mid
        
        if midSquare > num:
            r = mid - 1
        
        
            
        else:    
            ans = mid
            l = mid +1
    return ans
        
print(mySqrt(81))  
    