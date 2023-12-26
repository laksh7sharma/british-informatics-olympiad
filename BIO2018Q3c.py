from collections import deque
from itertools import permutations

def get_numbers_of_length_k(k):
    all_permutations = permutations(map(str, range(1, k + 1)))
    valid_permutations = filter(lambda x: len(x) == k, all_permutations)
    result = [''.join(permutation) for permutation in valid_permutations]
    return result

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

def createGroup(number):
    q = deque()
    visited = set()
    q.append(number)

    while len(q) > 0:
        el = q.popleft()
        if el not in visited:
            visited.add(el)
            n = neigbhours(el)
            q.extend(n)

    return visited

groups = []
visited = set()
numbers = get_numbers_of_length_k(5)

for number in numbers:
    if number not in visited:
        group = createGroup(number)
        visited = visited.union(group)
        groups.append(group)

print (len(groups))
