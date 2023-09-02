import itertools

n, k = map(int, input().split())
s = sorted(list(set(input().split())))
for item in itertools.combinations(s, k):
    print(" ".join(item))

