# 58. Length of the last word

s = "  fly me  to  the moon  "
n = len(s)
s = s.strip()

i = -1
count = 0
while i >= (-1 *n) and s[i] != " ":
    i -=1
    count += 1
    
print(f"Length of the last word is: {count}")