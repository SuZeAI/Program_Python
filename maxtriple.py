import heapq
import re
t = int(input())
for z in range(t) :
    n = int(input())
    main = ' ' + input().replace(' ', '  ') + ' '
    i = 8
    ans = 0
    cnt = 0
    while i > -9 and cnt < 4:
        s = '\d' * abs(i) + ' '
        if i < 0 :
            s = '-' + s
        elif i > 0 :
            s = ' ' + s
        else :
            i -= 1
            continue
        
        ls = [int(x) for x in re.findall(s, main)]
        if len(ls) + cnt >= 4:
            ans += sum(list(heapq.nlargest(3- cnt, ls)))
            break
        else:
            for k in ls:
                ans += k
                cnt += 1
        i -= 1
    print(ans)