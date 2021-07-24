# https://www.codechef.com/START6C/problems/ETUP

for T in range(int(input())):
    N,Q=map(int,input().split())
    n=list(map(int,input().split()))
    for z in range(Q):
        q=list(map(int,input().split()))
        num,na=0,list(filter(lambda a:a in range(q[0],q[1]+1),n))
        for i in range(0,len(na)-2):
            for j in range(i+1,len(na)-1):
                for k in range(j+1,len(na)):
                    if((na[i]+na[j]+na[k])%2==0): num+=1
        print(num)