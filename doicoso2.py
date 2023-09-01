def main():
    dic = {
        4: {0:0, 1:1, 2:2, 3:3},
        8: {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7},
        16: {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    }
    t: int = int(input())
    for _ in range(t):
        b: int = int(input())
        s = input()
        if b == 2:
            print(s)
        else:
            if b == 4:
                a = 2
            elif b == 8:
                a = 3
            else:
                a = 4
            ans = ""
            m = len(s) // a
            i = len(s)
            for _ in range(m):
                ans += str(dic[b][int(s[(i - a):i], 2)])
                i -= a
            if len(s[:i]) != 0:
                ans += str(dic[b][int(s[:i], 2)])
            print(ans[::-1])
            
    
main()