from multiset import Multiset
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    s1 = Multiset(map(int, input().split()))
    s2 = Multiset(map(int, input().split()))
    s3 = Multiset(map(int, input().split()))
    a = s1.intersection(s2).intersection(s3)
    print(" ".join(map(str, a)) if len(a) != 0 else "NO")
    
    