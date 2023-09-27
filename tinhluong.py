class Nhanvien(object):
    def __init__(self, manhanvien, ten, phong, luong):
        self.manhanvien = manhanvien
        self.ten = ten
        self.phong = phong
        self.luong = luong
    def __str__(self) -> str:
        return f"{self.manhanvien} {self.ten} {self.phong} {self.luong}"

def heso(chr, nam):
    if nam <= 3:
        if chr == 'A': return 10
        if chr == 'B': return 10
        if chr == 'C': return 9
        if chr == 'D': return 8
    elif nam <= 8:
        if chr == 'A': return 12
        if chr == 'B': return 11
        if chr == 'C': return 10
        if chr == 'D': return   9   
    elif nam <= 15:
        if chr == 'A': return 14
        if chr == 'B': return 13
        if chr == 'C': return 12
        if chr == 'D': return   11    
    else:
        if chr == 'A': return 20
        if chr == 'B': return 16
        if chr == 'C': return 14
        if chr == 'D': return   13
dc = {}
n = int(input())
for _ in range(n):
    s = input().split()
    dc[s[0]] = ' '.join(s[1:])

m = int(input())
nv= []
for _ in range(m):
    ma = input()
    ten = input()
    lg = int(input()) *  int(input()) * heso(ma[0], int(ma[1:3])) * 1000
    nv.append(Nhanvien(ma, ten, dc[ma[-2:]], lg))
for i in nv:
    print(i)
    
    