x,n = map(int,input().split())
p = n % 100
if p != 0:
    print((n//100 - x ) + 1)
else:
    print(n//100 - x)
