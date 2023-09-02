def ans(i, cnt, s="", bt=None):
    global check, ans_glo
    if check: return
    if i == len(cnt):
        k = 0
        kq = ""
        for ite in bt:
            if ite == "?":
                kq += s[k]
                k += 1
            else:
                kq += ite 
        ans_glo = kq                
        if(kq[3] == '/'):
            a, b, c = int(kq[:2]), int(kq[5:7]), int(kq[-2:])
            if a % b == 0 and a // b == c:
                check = True
        else:
            kq = kq[:9] + "=" + kq[9:]
            if eval(kq): check=True
        return
    if cnt[i] == 3:
        for item in ["+", "-", "*", "/"]:
            ans(i + 1, cnt, s + item, bt)
    elif cnt[i] in [0, 5, 10]:
        for item in range(1, 10):
            ans(i + 1, cnt, s + str(item), bt)
    else:
        for item in range(0, 10):
            ans(i + 1, cnt, s + str(item), bt)
    
    
t = int(input())
for _ in range(t):
    bt = input()
    cnt = []
    check=False
    ans_glo = None
    for idx, i in enumerate(bt):
        if i == "?":
            cnt.append(idx)
    ans(0, cnt, bt=bt)
    print(ans_glo if check else "WRONG PROBLEM!")