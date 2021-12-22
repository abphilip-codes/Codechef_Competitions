# https://www.codechef.com/START7C/problems/FODCHAIN

for T in range(int(input())):
    level=1
    e,k = map(int,input().split())
    while(e>=k): 
        e//=k
        level+=1
    print(level)