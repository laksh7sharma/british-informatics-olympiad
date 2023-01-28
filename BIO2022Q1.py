password = list(input())
for i in range(len(password) - 1, 0, -1):
    num = (26 + (ord(password[i]) - 64) - (ord(password[i-1]) - 64))
    if num > 26: num -= 26
    password[i] = chr(num + 64)
for char in password:
    print (char, end = "")
