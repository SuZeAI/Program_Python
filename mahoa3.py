def tong(s):
    return sum([ord(c) - 65 for c in s])
def xoay(s, so):
    ans = ""
    for i in s:
        ans += chr(65 + (ord(i) - 65 + so) % 26)
    return ans
n = int(input())
for _ in range(n):
    s = input()
    s1, s2 = s[:len(s)//2], s[len(s)//2:]
    s1 = xoay(s1, tong(s1))
    s2 = xoay(s2, tong(s2))
    ans = ""
    for i in range(len(s1)):
        ans += chr(65 + (ord(s1[i]) - 65 + ord(s2[i]) - 65) % 26)
    print(ans)
    
