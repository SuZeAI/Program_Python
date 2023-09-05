n = int(input())
ls = []
for i in range(n):
    tmp = list(map(int, input().split()))
    ls.append(tmp)
if n == 2:
    print(1, ls[0][1] - 1)
else:
    m = (ls[0][1] + ls[0][2] - ls[1][2])//2
    print(m, end=" ")
    for i in range(1, n):
        print(ls[0][i] - m, end=" ")