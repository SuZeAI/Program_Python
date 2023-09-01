class Matrix(object):
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.a = [[0] * m] * n
        
    def input(self):
        for i in range(self.n) :
            self.a[i] = [int(x) for x in input().split()]
            
    def solution(self):
        b = []
        for i in range(self.m) :
            x = []
            for j in range(self.n) :
                x.append(self.a[j][i])
            b.append(x)
        for i in range(self.n) :
            for j in range(self.n) :
                s = 0
                for z in range(self.m) :
                    s += self.a[i][z] * b[z][j]
                print(s, end = ' ')
            print()        

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    mx = Matrix(n, m)
    mx.input()
    mx.solution()