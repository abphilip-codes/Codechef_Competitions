# https://www.codechef.com/START6C/problems/ETUP

for T in range(int(input())):
    N,Q=map(int,input().split())
    n=list(map(int,input().split()))
    for z in range(Q):
        q,even,odd = list(map(int,input().split())),0,0
        diff = q[1]-q[0]+1
        odd = diff//2
        if q[0]%2!=0: odd+=1
        even = diff//2
        '''
        for i in n:
            if i in range(q[0],q[1]+1): 
                if(i%2==0): even+=1 
                else: odd+=1
        '''
        print(int(((even*(even-1)*(even-2))/6)+(odd*(odd-1))*even/2))
        '''
        for i in range(0,len(na)-2):
            for j in range(i+1,len(na)-1):
                for k in range(j+1,len(na)):
                    if((na[i]+na[j]+na[k])%2==0): num+=1
        '''