num = int(input())
res = 0
while num >0:
    res += num % 10
    num = num // 10
if res % 2 == 0:
    print("Vignesh")
else:
    print("Charan")
