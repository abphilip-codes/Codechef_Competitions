# https://www.codechef.com/START8C/problems/JAVELIN

for T in range(int(input())):
    (n,m,x)=map(int,input().split())
    fin=sel=[]
    a=list(map(int,input().split()))
    for i in range(n):
        if(a[i]>=m): fin.append(i+1)
    if(len(fin)<x):
        sel=sorted(a)[0-x:]
        fin=[]
        for z in sel:
            fin.append(a.index(z)+1)
    print(len(fin),end=" ")
    print(*sorted(fin))