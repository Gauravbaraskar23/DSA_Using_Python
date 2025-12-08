# 475 Koko eating banana

def getHours(piles , mid):
    ans =0 
    for pile in piles:
        ans += (pile +(mid-1))//mid
        
    return ans

def minEatingSpeed(piles, h):  # O(nlogmax)
    n = len(piles)
    
    l = 1
    r = max(piles)
    k = r
    
    while l <= r:  # O(logn)
        mid = (l+r)// 2
        
        if getHours(piles , mid) > h:
            l = mid+ 1
        
        else:
            k = mid
            r = mid-1
            
    return k

print(minEatingSpeed([3,6,7,11] , 8) )

