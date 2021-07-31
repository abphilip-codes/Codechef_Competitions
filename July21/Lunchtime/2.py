# https://www.codechef.com/LTIME98C/problems/REDALERT

for T in range(int(input())):
    n,d,h=map(int,input().split())
    l,check=list(map(int,input().split())),0
    for i in l:
        if(i==0): 
            if(check<d): check=0
            else: check-=d
            continue
        check+=i
        if(check>h):
            print("YES")
            break
    else: print("NO")