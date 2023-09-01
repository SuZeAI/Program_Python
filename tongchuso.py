n = list(map(int, list(input())))
cnt = 0
if len(n) == 1:
    print(1)
else:
    while len(n) != 1:
        tmp = sum(n)
        n = list(map(int, list(str(tmp))))
        cnt += 1
    print(cnt)