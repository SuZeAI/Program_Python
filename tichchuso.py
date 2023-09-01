from functools import reduce
t = int(input())
for _ in range(t):
    n = list(map(int,list(input().replace("0", "1"))))
    print(reduce(lambda a, b : a * b, n))