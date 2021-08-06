# https://www.codechef.com/AUG21C/problems/CHFINVNT

for T in range(int(input())):
    n,p,k = map(int,input().split())
    print(((n//k))*(p%k)+(p//k)+1)