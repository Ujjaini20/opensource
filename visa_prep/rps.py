v,c = input().split()
if v == c:
    print("NULL")
elif (v == 'S' and c == 'P') or (v == 'R' and c == 'S') or (v == 'P' and c == 'R'):
    print("Vignesh")
else:
    print("Charan")
