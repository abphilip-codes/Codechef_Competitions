# https://www.codechef.com/START7C/problems/CEILSUM

import math
for T in range(int(input())):
    a,b=map(int,input().split())
    if(a==b):print(0)
    else:print(math.ceil((b-min(a,b)-1)/2)+math.ceil((min(a,b)+1-a)/2))