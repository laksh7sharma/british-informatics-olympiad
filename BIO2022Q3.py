a,n = input().split()
n = int(n)
length = len(a)
total = 1
pref = [[] for i in range(length)]
prev = []
for i in range(length):
    letter = chr(97+i)
    for j,char in enumerate(a):
        if char == letter:
            prev.append(chr(65+j))
            break
        elif char < letter:
            prev.append(chr(65+j))
        else:
            prev.clear()
    pref[i].extend(prev)
    total *= len(prev)
    prev.clear()

step = 1
a = [0 for i in range(length)]
for i in range(length-1,-1,-1):
    previous = 0
    previous += step
    a[i] = previous
    step *= len(pref[i])

out = ""
i = 0

for k,item in enumerate(a):
    for el in pref[k]:
        i += item
        if i >= n:
            i -= item
            out += el
            break

print (out)
