# 151. Reverse words in a string and concatenated by a single space.

def reverseWords(s):
    s = s.strip()
    s = s.split()
    s.reverse()
    return " ".join(s)

s = "    the   sky is blue"
print(reverseWords(s))
