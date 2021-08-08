# https://www.codechef.com/AUG21C/problems/SPCTRIPS

for T in range(int(input())):
    n,c=int(input()),0
    for x in range(1,n+1):
        for y in range(x,n+1,x): c+=((n-(x+y))//y+1)
    print(c)