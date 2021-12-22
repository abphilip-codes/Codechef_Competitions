# https://www.codechef.com/LTIME98C/problems/BUTYPAIR

for T in range(int(input())):
    n,l,ans,i=int(input()),sorted(list(map(int,input().split()))),0,0
    while(i<n): 
        for j in range(i+1,n):
            if(l[i]!=l[j]): break
        ans,i=ans+((n-1)-(j-i-1))*(j-i),j
    print(ans)