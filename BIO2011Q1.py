s1, s2, n = input().split()
arr = [ord(s1) - 64, ord(s2) - 64]
n,i,repeat = int(n),2,0

while i < n and repeat == 0:
    arr.append(arr[-2] + arr[-1])
    if arr[-1] > 26: arr[-1] -= 26
    if arr[-1] == arr[0] and arr[-2] == arr[1]:
        repeat = i - 1
        arr.pop(-1)
        arr.pop(-1)
    i += 1

if repeat == 0:
    print(chr(arr[-1] + 64))
else:
    print (chr(arr[(n % repeat) - 1] + 64))