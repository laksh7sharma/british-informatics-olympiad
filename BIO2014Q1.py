arr = [i*2+1 for i in range(10005)]
cur = 3
while True:
    arr = [arr[i] for i in range(len(arr)) if (i+1) % cur != 0]
    try:
        cur = arr[arr.index(cur) + 1]
    except:
        break
a = int(input())
prev = arr[0]
for el in arr:
    if el > a:
        print(prev,el)
        break
    if a != el: prev = el