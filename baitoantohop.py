from itertools import combinations
n, k = map(int, input().split())

ls = sorted(list(set(map(int, input().split()))))
for i in combinations(ls, k):
    print(" ".join(map(str, i)))