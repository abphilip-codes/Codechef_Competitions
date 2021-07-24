# https://www.codechef.com/START6C/problems/CRICRANK

for T in range(int(input())):
    l1,l2,k=list(map(int,input().split())),list(map(int,input().split())),0
    for i in range(3): 
        if(l1[i]>l2[i]): k+=1  
        else: k-=1
    print("A") if(k>0) else print("B")