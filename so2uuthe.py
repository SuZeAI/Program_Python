t = int(input())
for _ in range(t):
    n = int(input())
    ls = ["1", "2"]
    while n > 0:
        a = ls.pop(0)
        nb2 = a.count("2")
        if nb2 > len(a)//2:
            print(a, end=" ")
            n -= 1
        ls.append(a + "0")
        ls.append(a + "1")
        ls.append(a + "2")
    print()
        
    