# https://www.codechef.com/JULY21C/problems/EITA 

for z in range(int(input())):
    d,x,y,z = map(int,input().split(" "))
    if(((d*y+(7-d)*z))>7*x): print(d*y+(7-d)*z)
    else: print(7*x)