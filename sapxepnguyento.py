a =  [0] * 1005
a[0] = 1
a[1] = 1
for i in range(2, 100):
    if a[i] == 0:
        for j in range(i*i, 1005, i):
            a[j] = 1

            
n = int(input())
ls = list(map(int, input().split()))
snt = sorted([i for i in ls if a[i] == 0])
for i in ls:
    if a[i] == 0:
        print(snt.pop(0), end=" ")
    else:
        print(i, end=" ")
