def f(str1):
    out = ""
    prev = None
    count = 0
    for char in str1:
        if char == prev or prev is None:
            count += 1
        else:
            out = out + dp[count] + prev
            count = 1
        prev = char
    if count > 0:
        out = out + dp[count] + char
    return out

dp = ["" for i in range(5000)]
dp[1],dp[5],dp[10],dp[50],dp[100],dp[500],dp[1000] = "I","V","X","L","C","D","M"
dp[4],dp[9],dp[40],dp[90],dp[400],dp[900] = "IV","IX","XL","XC","CD","CM"

specialNumbers = [1000, 500, 100, 50, 10, 5, 1]
specialLetters = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

for i in range(5000):
    if not dp[i]:
        for j in range(7):
            if i > specialNumbers[j]:
                dp[i] = specialLetters[j] + dp[i - specialNumbers[j]]
                break

str1, n = input().split()

for i in range(int(n)):
    str1 = f(str1)
print (str1.count("I"),str1.count("V"))