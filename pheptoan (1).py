
def result(ans):
    s = str(ls[0]) if ls[0] >= 0 else '('+ str(ls[0]) + ')'
    for i in range(1, n):
        s += ans[i - 1] +  (str(ls[i]) if ls[i] >= 0 else '('+ str(ls[i]) + ')')
    tmp = s
    tmp += "==" + str(m)
    if eval(tmp):
        kq.append(s + "=" + str(m))
        
def back(i, ans=""):
    if i == n - 1:
        result(ans)
        return
    for j in range(3):
        back(i + 1, ans + dau[j])

dau = ['+', '-', '*']    
n, m = map(int, input().split())
ls = list(map(int, input().split()))
kq = []
back(0)
if len(kq) == 0:
    print("IMPOSSIBLE")
else : 
    for i in kq: print(i)
