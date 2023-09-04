s =  input()
i = 0
ls = set()
ans = []
while i  + 1 < len(s):
    if s[i : i + 2] not in ls:
        ls.add(s[i: i + 2])
        ans.append(s[i : i + 2])
    i += 2
print(" ".join(ans))