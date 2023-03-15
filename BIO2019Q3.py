from bisect import bisect_left

def LIS(arr):
    ar = []
    for i in arr:
        ind = bisect_left(ar, i)
        if ind == len(ar):
            ar.append(i)
        else:
            ar[ind] = i
    return ar

n, pref = input().split()
n = int(n)
startorg = []
for char in pref:
    startorg.append(ord(char) - 64)
start = LIS(startorg)
choices = [i + 1 for i in range(n)]

def f(a, appended, previous):
    arr = a[:]
    if appended is not None:
        ind = bisect_left(arr, appended)
        if ind == len(arr):
            arr.append(appended)
        else:
            arr[ind] = appended
    total = 0
    if len(arr) >= 3:
        return 0
    for i in choices:
        if i in previous: continue
        prev = previous[:]
        prev.append(i)
        res = f(arr, i, prev)
        total += res
    if len(previous) == n:
        return 1
    return total

print (f(start, None, startorg[:]))


