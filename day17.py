def prime_factorization(N):
    factors = []
    
    while N % 2 == 0:
        factors.append(2)
        N //= 2
    
    p = 3
    while p * p <= N:
        while N % p == 0:
            factors.append(p)
            N //= p
        p += 2  
    
    if N > 1:
        factors.append(N)
    
    return factors

print(prime_factorization(18))      
print(prime_factorization(30))      
print(prime_factorization(49))      
print(prime_factorization(19))      
print(prime_factorization(64))      
print(prime_factorization(123456))  
