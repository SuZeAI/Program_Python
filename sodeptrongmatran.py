n, m = map(int, input().split())
ls = []
mn = None
mx = None
for i in range(n):
    tmp = list(map(int, input().split()))
    ls.append(tmp)
    mn = min(tmp) if mn is None else min(min(tmp), mn)
    mx = max(tmp) if mx is None else max(max(tmp), mx)
    
chek = True
ans = []
for i in range(n):
    for j in range(m):
        if ls[i][j] == mx - mn:
            ans.append((i, j))
            check = False
            

if check:
    print("NOT FOUND")    
else:
    print(mx - mn)
    for i, j in ans:
        print(f"Vi tri [{i}][{j}]")