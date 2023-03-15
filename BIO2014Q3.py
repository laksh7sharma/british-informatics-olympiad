from math import comb
str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
n = int(input())
depth = 1

while comb(36, depth) < n:
    n -= comb(36, depth)
    depth += 1
d = depth

def f(prev, n, depth):
    if depth == 0: return prev
    if prev == "": latest = 0
    else: latest = str1.index(prev[-1]) + 1
    for i in range(latest, 36):
        n -= comb(35 - i , depth - 1)
        if n <= 0:
            n += comb(35 - i, depth - 1)
            return f(prev + str1[i], n, depth - 1)

print (f("", n, depth))
