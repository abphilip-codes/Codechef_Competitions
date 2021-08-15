# https://www.codechef.com/START8C/problems/PENALTY

for T in range(int(input())):
    n=list(map(int,input().split()))
    a=b=0
    for i in range(len(n)):
        if(n[i]==1):
            if(i%2==0): a+=1
            else: b+=1 
    if(a>b): print(1) 
    elif(b>a): print(2)
    else: print(0)