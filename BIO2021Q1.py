def isPat(str1):
    if len(str1) == 1: return True
    for i in range(1,len(str1)):
        partA = str1[:i]
        partB = str1[i:]
        isPatstr1 = min(partA) > max(partB) and isPat(partA[::-1]) and isPat(partB[::-1])
        if isPatstr1: return True
    return False

str1,str2 = input().split()
arr = [str1,str2,str1+str2]
for element in arr:
    if isPat(element): print("YES")
    else: print ("NO")
