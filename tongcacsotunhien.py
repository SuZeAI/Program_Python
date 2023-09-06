kq = []
def bt(n, ans):
    if n == 0:
        kq.append(tuple(ans))
        return
    for j in range(n, 0, -1):
        if j <= ans[-1]:
            ans.append(j)
            bt(n - j, ans)
            ans.pop()
        
t = int(input())
for _ in range(t):
    n = int(input())
    kq.clear()
    bt(n, [n])
    print(len(kq))
    for tp in kq:
        s = " ".join(map(str, tp[1:]))
        print(f"({s})", end=" ")
    print()