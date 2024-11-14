t = int(input())
for _ in range(t):
    x,n = list(map(int,input().split()))
    res = x//10 * n
    print(res)
