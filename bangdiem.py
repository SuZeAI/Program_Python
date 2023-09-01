class HS(object):
    def __init__(self, name, id, meanscore):
        self.name = name
        self.id = id
        self.meanscore = round(meanscore + 0.01, 1)
        self.type = self.xeploai()
        
    def xeploai(self):
        if self.meanscore >= 9:
            return "XUAT SAC"
        if self.meanscore >= 8:
            return "GIOI"
        if self.meanscore >= 7:
            return "KHA"
        if self.meanscore >= 5:
            return "TB"
        return "YEU"


n = int(input())
ans = []
for i in range(n):
    id = "HS"
    if i + 1 < 10:
        id += '0' + str(i + 1)
    else: 
        id += str(i + 1)
    name = input()
    diem = list(map(float, input().split()))
    diem[0] = diem[0] * 2
    diem[1] = diem[1] * 2
    mean = sum(diem)/12
    ans.append(HS(name, id, mean))
ans.sort(key=lambda x : x.meanscore, reverse=True)
for i in ans:
    print(f"{i.id} {i.name} {i.meanscore} {i.type}")
                
        