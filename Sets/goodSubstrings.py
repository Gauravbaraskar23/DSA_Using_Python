# 1876. Substrings of Size Three with Distinct Characters

def countGoodSubstrings(s):
    n  = len(s)
    ans = 0
    
    for i in range(n-2):
        if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1]!= s[i+2]:
            ans += 1
            
    return ans

s = "xyzzaz"
print(countGoodSubstrings(s))