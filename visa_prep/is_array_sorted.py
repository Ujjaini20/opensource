n = int(input())
lt = list(map(int,input().split()))
if lt == sorted(lt):
    print("true")
else:
    print("false")
