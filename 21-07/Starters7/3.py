# https://www.codechef.com/START7C/problems/MAXARXOR

for T in range(int(input())):
    n,k=map(int,input().split())
    if(k>2**(n-1)): k=2**(n-1)
    print(((2**n)-1)*2*k)