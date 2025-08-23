def longestCommonPrefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    shortest = min(strs, key=len)
    
    for i, ch in enumerate(shortest):
        for word in strs:
            if word[i] != ch: 
                return shortest[:i]
    
    return shortest



print(longestCommonPrefix(["flower", "flow", "flight"])) 
print(longestCommonPrefix(["dog", "racecar", "car"]))    
print(longestCommonPrefix(["apple", "ape", "april"]))     
print(longestCommonPrefix([""]))                          
print(longestCommonPrefix(["alone"]))                     
print(longestCommonPrefix([]))                            
