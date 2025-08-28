def substringsWithKDistinct(s: str, k: int) -> int:
    def atMostK(s, k):
        n = len(s)
        left = 0
        freq = {}
        count = 0

        for right in range(n):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            count += (right - left + 1)

        return count

    if k == 0:
        return 0
    return atMostK(s, k) - atMostK(s, k - 1)

print(substringsWithKDistinct("pqpqs", 2))      
print(substringsWithKDistinct("aabacbebebe", 3)) 
print(substringsWithKDistinct("a", 1))           
print(substringsWithKDistinct("abc", 3))         
print(substringsWithKDistinct("abc", 2))         
print(substringsWithKDistinct("aaaa", 1))        
print(substringsWithKDistinct("abc", 5))        
