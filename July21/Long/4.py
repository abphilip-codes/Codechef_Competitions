# https://www.codechef.com/JULY21C/problems/MINNOTES

def repeat(a,b):
    while(b):
        a,b=b,a%b
    return a
def re(a):
    n1=a[0]
    n2=a[1]
    den=repeat(n1,n2)
    for z in range(2,n):
        den=repeat(den,a[z])
    return den
for T in range(int(input())):
    a1 = []
    n, a = int(input()),list(map(int,input().split(" ")))
    a.sort(reverse=True)
    for z in range(0,n):
        if(a[z]%min(a)!=0):
            a[z]=min(a)
            break
    else: a[a.index(max(a))]=min(a)
    if(n>=2): den = re(a)
    else: den = a[0]
    print(int(sum(a)/den))