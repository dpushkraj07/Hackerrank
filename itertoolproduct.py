from itertools import product

a = []
b = []
l = []
a = map(int,input().split())
b = map(int,input().split())

l = list(product(a,b))
print(*l)
