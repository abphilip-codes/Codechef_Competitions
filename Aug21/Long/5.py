# https://www.codechef.com/AUG21C/problems/ARRFILL

for T in range(int(input())):
    n,m=map(int,input().split())
    x=y=[]
    A=[0]*n
    for i in range(m):
        X,Y=map(int,input().split())
        x.append(X)
        y.append(Y)
    