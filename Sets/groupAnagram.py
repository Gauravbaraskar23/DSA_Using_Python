# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
def sortString(s):
    s1 = list(s)
    s1.sort()
    return "".join(s1)
    # return "".join(sorted(s))

def groupAnagrams(strs):
    dict1 = {}
    
    for s in strs:
        key = sortString(s)
        if key in dict1:
            dict1[key].append(s)
        else:
            dict1[key] = [s]
    
    return list(dict1.values())
strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))