# 242. Valid Anagram

# def areAnagram(s, t):
#     if len(s) != len(t):
#         return False
#     return sorted(s) == sorted(t)
#     # return set(s) == set(t)

def areAnagram(s, t):
    if len(s) != len(t):
        return False
    frq= {}
    
    for i in s:
        if i not in frq:
            frq[i] = 1
        else:
            frq[i] += 1
    
    for i in t:
        if i not in frq:
            return False
        else:
            frq[i] -=1
    
    for i in frq.values():
        if i != 0:
            return False
    
    return True
    
s = "anagram"
t= "nagaram"
print(areAnagram(s,t))
