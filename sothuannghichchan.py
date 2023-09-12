t = int(input())

for _ in range(t):
    n = int(input())
    ls = ["2", "4", "6", "8"]
    while True:
        front = ls.pop(0)
        if int(front + front[::-1]) >= n:
            break
        else:
            print(front + front[::-1], end=" ") 
        ls.append(front + "0")
        ls.append(front + "2")
        ls.append(front + "4")
        ls.append(front + "6")
        ls.append(front + "8")
        
    print()