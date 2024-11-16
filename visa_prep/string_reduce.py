str1 = input()
c = 1
for i in range(1,len(str1)):
    if str1[i] == str1[i-1]:
        c += 1
    else:
        print(str1[i-1]+str(c),end="")
        c = 1
print(str1[-1]+str(c),end="")
    
