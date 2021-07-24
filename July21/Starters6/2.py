# https://www.codechef.com/START6C/problems/THREDICE

for T in range(int(input())):
    a,b=map(int,input().split())
    s="{:.10f}".format((6-(a+b))/6)[0:8]
    print(s) if(a+b<6) else print(0)