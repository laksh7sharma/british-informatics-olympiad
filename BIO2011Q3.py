arr = []
previous = 1
for i in range(20):
    if i % 2 == 1:
        arr.append(previous*9)
        previous *= 9
    else:
        arr.append(previous)

nthNumber = int(input())
for i,num in enumerate(arr):
    nthNumber -= num
    if nthNumber < 0:
        digits = i + 1
        nthNumber += num
        break

nthNumber -= 1
odd = digits % 2 == 1
i = 0
arr = [0 for j in range(digits)]
count = 0

while count < digits // 2:
    increment = num // 9
    ind = (nthNumber - i) // increment
    i += ind * increment
    num = increment
    arr[count], arr[digits - 1 - count] = ind + 1, 9 - ind
    count += 1

if odd: arr[digits // 2] = 5

for item in arr:
    print (item , end = "")