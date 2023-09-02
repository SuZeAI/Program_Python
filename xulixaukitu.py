s1, s2 = list(map(str.lower, input().split())), list(map(str.lower, input().split()))
print(" ".join(sorted(list((set(s1).union(set(s2)))))))
print(" ".join(sorted(list((set(s1).intersection(set(s2)))))))