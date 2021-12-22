# https://www.codechef.com/AUG21C/problems/OLYRANK

for T in range(int(input())):
    l=list(map(int,input().split()))
    print('1') if(sum(l[0:3])>sum(l[3:6])) else print('2')