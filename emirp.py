a = [0] * 1000001
def era():
    a[0] = a[1] = 1
    for i in range(2, 1000):
        if a[i] == 0:
            for j in range(i * i , 1000001, i):
                a[j] = 1
                
def main():
    t = int(input())
    era()
    for _ in range(t):
        n = int(input())
        s = []
        for i in range(13, n):
            if a[i] == 0 and str(i) != str(i)[::-1] and a[int(str(i)[::-1])] == 0 and int(str(i)[::-1]) < n:
                if i not in s:
                    s.extend([i, int(str(i)[::-1])])
        print(" ".join(map(str, (s))))
main()