s =  input()
i = 0
ls = set()
while i  + 1 < len(s):
    ls.add(s[i: i + 2])
    i += 2
print(" ".join(sorted(list(ls))))   