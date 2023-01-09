def isPalindromic(str1):
    total = 0
    for i in range(1,len(str1)//2+1):  # iterates till the midpoint
        if str1[:i] == str1[len(str1)-i:]:  # compares the 2 identical length parts on opposite sides of string
            total = total + 1 + isPalindromic(str1[i:len(str1)-i])
    return total
print (isPalindromic(input()))
