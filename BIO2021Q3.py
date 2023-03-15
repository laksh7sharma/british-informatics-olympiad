from collections import deque
str1 = input()
qu = deque()
qu.append(["A",1])
visited = {"A"}
found = False
while not found:
    el = qu.popleft()
    if el[0] == str1:
        found = True
        print (el[1])
    else:
        if len(el[0]) >= 2:
            SwapVariable = el[0][1] + el[0][0] + el[0][2:]
            if SwapVariable not in visited:
                qu.append([SwapVariable, el[1] + 1])
                visited.add(SwapVariable)
            RotateVariable = el[0][1:] + el[0][0]
            if RotateVariable not in visited:
                qu.append([RotateVariable, el[1] + 1])
                visited.add(RotateVariable)
        AddVariable = el[0] + chr(ord("A") + len(el[0]))
        if AddVariable not in visited:
            qu.append([AddVariable, el[1] + 1])
            visited.add(AddVariable)