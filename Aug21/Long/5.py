# https://www.codechef.com/AUG21C/problems/ARRFILL

import math
for T in range(int(input())):
    n,m=map(int,input().split())
    l,z,k,al,ans=[],0,n,1,0
    for i in range(m): l.append(list(map(int,input().split())))
    l.sort(reverse=True)
    while(k>0 and z<m):
        al=(al*l[z][1])//math.gcd(al,l[z][1])
        ans,k,z=ans+l[z][0]*(k-(n//al)),n//al,z+1
    print(int(ans))