i,r = map(int , input().split())
ir,rr = 1 + i/100,r/100
paid,debt = 0,100
def up(num):
    a = round(num,2)
    if a < num:
        a += 0.01
    return a
def interest(d):
    c = d*ir
    c = round(c,8)
    return up(c)
def repayment(d):
    global paid
    b = up(d*rr)
    b = round(b,8)
    a = max(b,50)
    if a < d:
        paid += a
        return d - a
    else:
        paid += d
        return 0

while debt > 0:
    debt = interest(debt)
    debt = repayment(debt)
print (paid)
# 22 minutes