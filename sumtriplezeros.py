def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ls = list(map(int, input().split()))
        ls.sort()
        cnt  = 0
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            x = ls[i]
            while l < r:
                if x + ls[l] + ls[r] == 0:
                    cnt += 1
                    l += 1
                    r -= 1
                elif x + ls[l] + ls[r] > 0:
                    r -= 1
                else:
                    l += 1
                
        print(cnt)
    
    
main()