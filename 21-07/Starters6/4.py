# https://www.codechef.com/START6C/problems/ETUP

for T in range(int(input())):
    N,Q=map(int,input().split())
    n=list(map(int,input().split()))
    for z in range(Q):
        q = list(map(int,input().split()))
        diff = q[1]-q[0]+1
        odd=even=diff//2
        if(diff%2!=0): 
            if(q[0]%2!=0): odd=even+1
            else: even=odd+1
        print(int(((even*(even-1)*(even-2))/6)+(odd*(odd-1))*even/2))