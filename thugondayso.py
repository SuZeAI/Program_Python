from collections import deque
if __name__ == "__main__":
    n = int(input())
    ls = list(map(int, input().split()))
    ls1 = deque()
    for i in range(n):
        if len(ls1) == 0:
            ls1.append(ls[i])
        else:
            if (ls1[-1] + ls[i]) % 2 == 0:
                ls1.pop()
            else:
                ls1.append(ls[i])
    print(len(ls1))
    