import sys

def cin():
    for i in sys.stdin.read().split():
        yield i

cn = cin()
while True:
    n = int(next(cn))
    if n == 0:
        break
    mn = 1e101
    mx = 0
    for i  in range(n):
        tmp = int(next(cn))
        mn = min(mn, tmp)
        mx = max(mx, tmp)
    print(f"{mn} {mx}" if mn != mx else "BANG NHAU")