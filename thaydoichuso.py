def main():
    t = int(input())
    for _ in range(t):
        p, q = input().split()
        s =  input().strip()
        if " " in s: s, s1 = s.split()
        else: s1 = input().strip()
        print(int(s.replace(max(p, q), min(p, q))) + int(s1.replace(max(p, q), min(p, q))), end=" ")
        print(int(s.replace(min(q, p), max(p, q))) + int(s1.replace(min(q, p), max(p, q))))

main()