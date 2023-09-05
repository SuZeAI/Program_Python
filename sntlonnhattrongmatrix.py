a = [0] * 1005
a[0] = 1
a[1] = 1
for i in range(2, 100):
    if a[i] == 0:
        for j in range(i * i , 1005, i):
            a[j] = 1
        
        
n, m = map(int, input().split())
index = []
ans = None
for i in range(n):
    ls = list(map(int, input().split()))
    for j in range(m):
        if a[ls[j]] == 0:
            if ans is None or ls[j] > ans:
                index.clear()
                ans = ls[j]
                index.append((i, j))
            elif ls[j] == ans:
                index.append((i, j))
if ans is None:
    print("NOT FOUND")
else:                
    print(ans)
    for i, j in index:
        print(f"Vi tri [{i}][{j}]")    
    
