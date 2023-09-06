n = int(input())
ls = list(map(int, input().split()))
ls.sort()
print(max(ls[0] * ls[1] * ls[2], ls[0] * ls[1], ls[-1] * ls[-2], ls[-1] * ls[-2] * ls[-3], ls[0] * ls[1] * ls[-1]))