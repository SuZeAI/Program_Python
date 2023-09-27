with open("DATA.in", "r") as f:
    s = f.read().replace('\n', " ").split()
    ans = []
    for i in s:
        if i.isdigit() and int(i) > int(1e9):
           ans.append(i)
        elif not i.isdigit():
            ans.append(i)
    print(" ".join(sorted(ans)))
    