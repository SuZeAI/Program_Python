a = 3
b = a
a += 1
a = 3
print(id(a))
print(id(b))
print(a is b)
print(b is a)