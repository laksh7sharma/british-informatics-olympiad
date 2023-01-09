def f(n1,n2):
    if n1 == n2: return n1
    return 6 - (n1 + n2)
convert = {"B" : 1, "G" : 2, "R" : 3, 1 : "B", 2 : "G", 3 : "R"}
inp = list(str(input()))
arr = [convert[el] for el in inp]
while len(arr) > 1:
    arr = [f(arr[i], arr[i+1]) for i in range(len(arr)-1)]
print (convert[arr[0]])