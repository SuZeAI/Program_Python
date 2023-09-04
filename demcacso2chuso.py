s =  input()
k = int(input())
i = 0
ls = set()
mp = {}
while i  + 1 < len(s):
    ls.add(s[i: i + 2])
    if s[i : i + 2] not in mp:
        mp[s[i : i + 2]] = 0
    mp[s[i : i + 2]] += 1
    i += 2
check = False
for item in sorted(list(ls)):
   if mp[item] >= k:
        print(item, mp[item])
        check = True
    
if not check:
    print("NOT FOUND")
    