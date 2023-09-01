def main():
    t = int(input())
    for _ in range(t):
        s = input() + "suzeai"
        mn = 0
        num = ""
        for i in s:
            if i.isnumeric():
                num += i
            else:
                if len(num) != 0:
                    mn = max(mn, int(num))
                num = ""
        print(mn)       
main()