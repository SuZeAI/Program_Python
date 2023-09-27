mod = 1000
class find(object):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def mul(a, b):
    r = find(0, 0)
    r.x = (a.x * b.x + 5 * a.y * b.y) % mod
    r.y = (a.x * b.y +  a.y * b.x) % mod
    return r

def pow(a, b):
    if b == 0: return find(1, 0)
    if b & 1: return mul(pow(a, b - 1), a)
    p = pow(a, b>>1)
    return mul(p, p)

x = find(3, 1)
for i in range(int(input())):
    n = int(input())
    print(f"Case #{i + 1}: {str(pow(x, n).x * 2 % mod - 1).zfill(3)}")

        