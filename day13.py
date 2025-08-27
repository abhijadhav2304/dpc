def longest_palindrome(s: str) -> str:
  
    if len(s) == 1:
        return s
    start, max_len = 0, 1   
    def expand(l: int, r: int):
        nonlocal start, max_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1
    
    for i in range(len(s)):
        expand(i, i)      
        expand(i, i + 1)   
    
    return s[start:start + max_len]

print(longest_palindrome("babad"))  
print(longest_palindrome("cbbd"))   
print(longest_palindrome("a"))     
print(longest_palindrome("aaaa"))   
print(longest_palindrome("abc"))    
