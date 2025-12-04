# 344. Reverse String :
# input : ["h",'e',"l", "l","o"]
# output : ["o", "l","l","e","H"]

# def revString(s):
#     return s[::-1]

# OR

def revString(s):
    i = 0
    j = len(s) -1
    
    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i +=1
        j -=1
    return s
    


s = ["h",'e',"l", "l","o"]
print(revString(s))