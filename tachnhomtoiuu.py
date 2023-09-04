n, k = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
ans = 1
for i in range(1, n):
    if ls[i] - ls[i - 1] > k:
        ans += 1
print(ans)        