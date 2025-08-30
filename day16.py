import math

def lcm(n, m):
    return (n * m) // math.gcd(n, m)
N, M = map(int, input().split())

print(lcm(N, M))
