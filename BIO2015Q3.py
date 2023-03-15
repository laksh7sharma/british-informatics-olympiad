from math import factorial

def f(nums):
    r = 1
    b = length - len(nums)
    for key, value in a.items():
        if value - nums.count(key) > 0: r *= factorial(value - nums.count(key))
    return int(factorial(b) / r)

a, b, c, d, n = map(int, input().split())

a = {1: a, 2: b, 3: c, 4: d}
length = 0
const = 1
for value in a.values():
    length += value
pref = []
i = 0

while len(pref) < length:
    for item in a.keys():
        if a[item] > pref.count(item):
            pref.append(item)
            tot = f(pref)
            i += tot
            if i >= n:
                i -= tot
                break
            pref.pop(-1)

for char in pref:
    print(chr(char + 64), end="")
