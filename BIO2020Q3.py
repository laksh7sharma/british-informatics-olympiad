from functools import lru_cache

@lru_cache(maxsize=None)
def f(recent,count,remaining):
    global letters, limit
    total = 0
    if count <= limit:
        if remaining == 0:
            total = 1
        else:
            for char in letters:
                if char == recent:
                    total += f(recent, count + 1, remaining - 1)
                else:
                    total += f(char, 1, remaining - 1)
    return total

p,limit,maxLen = map(int , input().split())
n = int(input())
letters = [chr(65+i) for i in range(p)]

i = 1
repeat = 0
pref = []
prev = None
rem = maxLen

while rem > 0:
    rem -= 1
    copy = pref[:]
    for letter in letters:
        if letter == prev: repeat += 1
        else: repeat = 1
        if repeat > limit: continue
        copy.append(letter)
        tot = f(letter,repeat,rem)
        i += tot
        if i > n:
            pref = copy[:]
            prev = letter
            i -= tot
            break
        copy.pop()

for char in pref:
    print (char, end = "")