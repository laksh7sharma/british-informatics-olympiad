arr = list(map(int , str(input())))
arr = [str(j) for j in arr]
flag = False
for i in range(2,10):
    num = int("".join(arr))
    num *= i
    new = [k for k in str(num)]
    copy = arr[:]
    copy.sort()
    new.sort()
    if copy == new:
        print (i, end=" ")
        flag = True
if not flag:
    print ("NO")