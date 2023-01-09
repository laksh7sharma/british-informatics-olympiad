from math import gcd
l,m,r,s = 1,0,0,1
def lowestForm(fraction):
    n1,n2 = fraction
    return n1//gcd(n1,n2), n2//gcd(n1,n2)

promenade = list(str(input()))
fraction = (1,1)
previous = promenade[0]

for char in promenade:
    if char == "L": l, m = fraction
    else: r,s = fraction
    fraction = lowestForm((l+r,m+s))

print (f"{fraction[0]} / {fraction[1]}")