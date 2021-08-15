# https://www.codechef.com/START8C/problems/THREEPTS

for T in range(int(input())):
    ax,ay=map(int,input().split())
    bx,by=map(int,input().split())
    cx,cy=map(int,input().split())
    print("YES") if((ax==bx or ay==by) and (bx==cx or by==cy)) else print("NO")