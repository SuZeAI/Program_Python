import math
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    gc = math.gcd(a, b)
    print(a * b// gc, gc)   