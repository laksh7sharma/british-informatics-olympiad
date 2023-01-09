# sieve = [1 for i in range(1000000)]
# for i in range(2,1000000):
#     if sieve[i] == 1:
#         for j in range(i,1000000,i):
#             sieve[j] *= i
# print (sieve[int(input())])

# num = int(input())  # alternative faster approach
# a = set()
# i = 2
# while i <= num:
#     while num % i == 0:
#         a.add(i)
#         num = num // i
#     i += 1
#     if i == num: a.add(i)
# output = 1
# for num in a:
#     output *= num
# print (output)