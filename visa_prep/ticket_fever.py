t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    print(n-m) if n>m else print(0)
