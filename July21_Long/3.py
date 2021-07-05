# https://www.codechef.com/JULY21C/problems/XXOORR

for T in range(int(input())):
    a1 = []
    a2 = []
    a3 = 0
    n,k = map(int,input().split(" "))
    a = list(map(int,input().split(" ")))
    p = 0
    for z in range(n): a1.append(0) 
    while(a!=a1):
        a2 = []
        for z in range(n):
            if(a[z]<=a[z]^(2**p) or a[z]==0): a2.append(0)
            else: 
                a[z]=a[z]^(2**p)
                a2.append(1)
        a3 = a3 + sum(a2)//k + sum(a2)%k
        p+=1
    print(a3)