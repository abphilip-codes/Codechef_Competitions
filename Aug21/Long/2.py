# https://www.codechef.com/AUG21C/problems/PROBDIFF

for T in range(int(input())):
    a=list(map(int,input().split()))
    if(a[0]!=a[1] and a[2]!=a[3]): print(2)
    elif(a[0]!=a[2] and a[1]!=a[3]): print(2)
    elif(a[0]!=a[3] and a[2]!=a[1]): print(2)
    elif(a[0]!=a[1] or a[2]!=a[3]): print(1)
    elif(a[0]!=a[2] or a[1]!=a[3]): print(1)
    elif(a[0]!=a[3] or a[2]!=a[1]): print(1)
    else: print(0)