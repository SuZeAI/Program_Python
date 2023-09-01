t = int(input())
for _  in range(t):
    print(f"Test {_ + 1}: ", end="")
    s1 = sorted(list(input()))
    s2 = sorted(list(input()))
    print("YES" if s1 == s2 else "NO")