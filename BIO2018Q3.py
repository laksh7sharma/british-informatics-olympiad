from collections import deque

def neigbhours(str1):
    possible = []
    str1 = list(str1)
    for i in range(len(str1) - 1):
        n2,n3 = str1[i], str1[i + 1]
        n1 = -1 if i == 0 else str1[i - 1]
        n4 = 10000 if i + 2 == len(str1) else str1[i + 2]
        n1, n2, n3, n4 = int(n1), int(n2), int(n3), int(n4)
        if n2 < n1 < n3 or n3 < n1 < n2 or n2 < n4 < n3 or n3 < n4 < n2:
            copy = str1[:]
            copy[i], copy[i + 1] = copy[i + 1], copy[i]
            res = ""
            for item in copy:
                res += item
            possible.append(res)
    return possible

g = dict()
length = input()
start = input()

q = deque()
visited = set()
q.append(start)

while len(q) > 0:
    el = q.popleft()
    if el not in visited:
        visited.add(el)
        n = neigbhours(el)
        g[el] = n
        q.extend(n)

def floyd_warshall(g):
    n = len(g.keys())
    shortest = [[float("inf") for i in range(n)] for j in range(n)]
    arr = [el for el in g.keys()]
    for k,v in g.items():
        ind = arr.index(k)
        shortest[ind][ind] = 0
        for item in v:
            inde = arr.index(item)
            shortest[ind][inde] = 1
            shortest[inde][ind] = 1

    for i in range(n):
        for j in range(n):
            for k in range(n):
                shortest[i][k] = min(shortest[i][k], shortest[i][j] + shortest[j][k])

    return max(shortest[arr.index(start)])

def bfs(g):  # this also works
    visited = set()
    maxi = -1
    q = deque()
    q.append((start, 0))
    while len(q) > 0:
        node, dist = q.popleft()
        visited.add(node)
        maxi = max(maxi, dist)
        for neigbhour in g[node]:
            if neigbhour not in visited:
                q.append((neigbhour, dist + 1))

    return maxi

print (bfs(g))