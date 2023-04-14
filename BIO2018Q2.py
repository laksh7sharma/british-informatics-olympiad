from collections import deque
q = deque()
n, word = input().split()
n = int(n)
for char in range(65, 91):
    q.append(chr(char))
q1 = q.copy()
q2 = deque()

while len(q) > 0:
    tempn = n % len(q)
    tempn = (tempn - 1) % len(q)
    for i in range(tempn):
        q.rotate(-1)
    el = q.popleft()
    q2.append(el)

for i in range(6):
    print (q2[i], end ="")
print ("\n".strip())
for char in word:
    while q1[0] != char:
        q1.rotate(-1)
        q2.rotate(-1)
    print (q2[0], end = "")
    q2.rotate(-1)
