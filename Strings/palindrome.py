# 125. Valid Palindrome

# def palindrome(pal):
#     return pal == pal[::-1]

# OR

def isAlphaNumeric(s):
    x = ord(s)
    
    if 97<= x <= 122 or 65 <= x <=90 or 48 <= x <= 57:
        return True
    return False


def palindrome(s):
    s = s.lower()
    i = 0
    j = len(s) -1
    
    while i<j :
        if not isAlphaNumeric(s[i]):
            i += 1
        elif not isAlphaNumeric(s[j]):
            j -= 1
        elif s[i] == s[j]:
            i +=1 
            j -=1
        else:
            return False
    return True
    
    
s = input("Enter String: ")
# pal = "madam"
print(palindrome(s))