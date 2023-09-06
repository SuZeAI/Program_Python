import sys
def stin():
    for i in sys.stdin.read().split():
        yield i
        
cin = stin()

n = int(next(cin))
ls = []
for i in range(n):
    ls.append(int(next(cin)))
i = 1
mx = max(ls)
check = True
while i < mx:
    if i not in ls:
        print(i)
        check= False
    i += 1

if check:
    print("Excellent!")