t = int(input())
for _ in range(t):
    tmp = input()
    s = ""
    num = 0
    for i in tmp:
        if i.isalpha():
            s += i
        elif i.isnumeric():
            num += int(i)
    print("".join(sorted(list(s))) + str(num))