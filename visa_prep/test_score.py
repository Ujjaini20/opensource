n,x,y = map(int,input().split())
print("YES") if (y%x == 0 and y <= x*n)else print("NO")
