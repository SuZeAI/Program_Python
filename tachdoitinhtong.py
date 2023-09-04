s = input()
while len(s) != 1:
    n = len(s)
    tmp = int(s[:n//2]) + int(s[n//2:])
    print(tmp)
    s = str(tmp)
