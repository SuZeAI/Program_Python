from itertools import permutations

a = list(input())
for i in permutations(a):
    print("".join(i))