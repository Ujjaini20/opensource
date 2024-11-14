x,y,z = map(int,input().split())
left_weight = z - y
i = 1
while ( i >= 1):
    mangoes_weight = i * x
    if mangoes_weight > left_weight:
        print(i-1)
        break
    i += 1
