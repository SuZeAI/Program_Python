import itertools 
def tinh(ls):
    ans = 0
    for i, v in enumerate(ls):
        if i % 5 == 0:
            ans += v
        elif i % 5 == 1:
            ans -= 2 * v
        elif i % 5 == 2:
            ans += 3 * v
        elif i % 5 == 3:
            ans -= 4 * v
        elif i % 5 == 4:
            ans += 5 * v
    return ans

t = int(input())
for _ in range(t):
    ans = None
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))
    for item in itertools.combinations(ls, 5 * k):
        tin = tinh(list(item))
        ans = tin if ans is None else max(ans, tin)
    print(ans)