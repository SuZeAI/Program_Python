while True:
    s = input()
    if s == "-1":
        break
    l, r = map(int, s.split())
    n = int(input())
    st = set()
    for i in range(2, n + 1):
        m = l//i * i 
        while m < l:
            m += i
        while m <= r:
            if m not in st:
                st.add(m)
            m += i

    print(r - l + 1 - len(st))    
