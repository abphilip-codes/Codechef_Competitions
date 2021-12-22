# https://www.codechef.com/LTIME98C/problems/CHFSPL

for T in range(int(input())):
    l=sorted(list(map(int,input().split())))
    print(sum(l[::-1][0:2]))