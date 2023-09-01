BIT = [0] * 1005

def upd(i, k):
    while i < 1005:
        BIT[i] += k
        i += i & -i
def qr(i):
    sm = 0
    while i > 0:
        sm += BIT[i]
        i -= i & -i
    return sm
        
n = int(input())
ls = list(map(int, input().split()))
r = []
idx = 1
dic = dict()
for i in ls:
    if i not in dic:
        r.append(idx)
        dic[i] = idx
        idx += 1
    else:
        r.append(dic[i])
ans = sorted(list(zip(ls, r)), key=lambda x : x[0], reverse=True)
res = 0
for i, (a, b) in enumerate(ans):
    upd(b, 1)
    res += qr(b - 1)
print(res)