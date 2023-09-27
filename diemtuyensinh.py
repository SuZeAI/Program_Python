import math
class hs(object):
    def __init__(self, ma, ten, tong, tt) -> None:
        self.ma = ma
        self.ten = ten
        self.tong = tong
        self.tt = tt
    def __str__(self) -> str:
        return f"{self.ma} {self.ten} {round(self.tong, 1)} {self.tt}"
    
def point(toc, kv):
    ks = 0
    if toc != "Kinh": ks += 1.5
    if kv == 3: ks +=  0
    if kv == 1: ks += 1.5
    if kv == 2: ks += 1
    if toc == "Kinh": ks += 0 
    return ks

n = int(input())
ans = []
for _ in range(n):
    ma = "TS" + str(_ + 1).zfill(2)
    ten = " ".join(map(str.title, (input().split())))
    diem = float(input()) 
    toc = input()
    kv = int(input())
    diem += point(toc, kv)
    tt = "Do" if diem >= 20.5 else "Truot"
    ans.append(hs(ma, ten, diem, tt))
ans.sort(key=lambda x : x.tong, reverse=True)
for i in ans:
    print(i)
    