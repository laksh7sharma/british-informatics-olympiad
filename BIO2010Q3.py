from collections import deque


def f1(first, chosen):
    elements = first[:]
    elements[chosen] = numbers[chosen]
    return elements


def f2(e, chosen):
    elements = e[:]
    elements[chosen] = 0
    return elements


def f3(e, chosen1, chosen2):
    copy = e[:]
    while copy[chosen1] < numbers[chosen1] and copy[chosen2] > 0:
        copy[chosen1] += 1
        copy[chosen2] -= 1
    return copy


qu = deque()
number, required = map(int, input().split())
numbers = list(map(int, input().split()))
permutations = []
visited = []
arr = [0 for i in range(number)]
for i in range(number):
    for j in range(number):
        if i > j:
            permutations.append([i, j])
            permutations.append([j, i])

ops = [f1, f2, f3]

for i, el in enumerate(numbers):
    copy = arr.copy()
    copy[i] = el
    qu.append([copy, 1])

while len(qu) > 0:
    el1 = qu.popleft()
    elements, num = el1[0][:], el1[1]
    if elements not in visited:
        visited.append(elements)
        if required in elements:
            print(num)
            break

        for function in ops:
            copy = elements[:]
            if function == f3:
                for permutation in permutations:
                    other = function(elements, permutation[0], permutation[1])
                    copy = other[:]
                    if copy not in visited:
                        qu.append([copy, num + 1])
            else:
                for i, el in enumerate(numbers):
                    other = function(elements, i)
                    copy = other[:]
                    if copy not in visited:
                        qu.append([copy, num + 1])
