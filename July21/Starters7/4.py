# https://www.codechef.com/START7C/problems/CEILSUM

import math
for T in range(int(input())):
    a,b=map(int,input().split())
    maximum=-32700
    for x in range(min(a,b),max(a,b)+1):
        if(math.ceil((b-x)/2)+math.ceil((x-a)/2)>maximum): 
            maximum=math.ceil((b-x)/2)+math.ceil((x-a)/2)
    print(maximum)