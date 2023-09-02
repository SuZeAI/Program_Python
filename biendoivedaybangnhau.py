import sys

def nxt():
    for i in sys.stdin.read().split():
        yield int(i)
        
cin = nxt()

n = next(cin)
a = []
for i in range(n):
    a.append(next(cin))
ans = 1e9
for idx, value in enumerate(a):
    tmp = 0
    for id, vl in enumerate(a):
        if id != idx:
            tmp +=  abs(vl - value)
    if tmp < ans:
        ans = tmp
        ans_idx = idx
print(f"{ans} {a[ans_idx]}")