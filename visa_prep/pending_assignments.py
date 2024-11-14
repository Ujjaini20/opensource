x,y,z = map(int,input().split())
time_req = x * y
total_time = z * 24 * 60
if time_req <= total_time:
    print("YES")
else:
    print("NO")
