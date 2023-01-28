str1 = input()
p1 = str1[:(len(str1)+1)//2]
while True:
    p1 = str(int(p1)+1)
    if len(str1) % 2 == 0: out = p1 + p1[::-1]
    else: out = p1 + p1[::-1][1:]
    if int(out) > int(str1): break
print (out)
