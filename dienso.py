t = int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    l = min(ls)
    r = max(ls)
    cnt = 0
    for i in range(l, r + 1):
        if i not in ls:
           cnt += 1
           
    print(cnt) 