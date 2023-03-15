from collections import deque

maxi,num,required = map(int , input().split())

sieve = [True for i in range(maxi+5)]
visited = [False for i in range(maxi+5)]

for i,el in enumerate(sieve):
    if i > 1:
        if el:
            for j in range(2*i,maxi+5,i):
                sieve[j] = False

qu = deque()
qu.append([num,1])

while len(qu) > 0:
    el = qu.popleft()
    if el[0] == required:
        print (el[1])
        break
    for i in range(20):
        n1 = el[0] + (1 << i)
        n2 = el[0] - (1 << i)
        if n1 <= maxi and sieve[n1] and not visited[n1]:
            qu.append([n1 , el[1] + 1])
            visited[n1] = True
        if n2 >= 2 and sieve[n2] and not visited[n2]:
            qu.append([n2, el[1] + 1])
            visited[n2] = True
