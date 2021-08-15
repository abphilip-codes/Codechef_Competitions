# https://www.codechef.com/START8C/problems/THREEPTS

for T in range(int(input())):
    ax,ay=map(int,input().split())
    bx,by=map(int,input().split())
    cx,cy=map(int,input().split())
    turn=0
    if(ax==bx or ay==by): turn+=0
    else: turn+=1
    if(cx==bx or cy==by): 
        if(cx==bx and ax==bx): 
            if(bx not in range(min(ax,cx),max(ax,cx)+1)): turn=2
            turn+=0
        elif(cy==by and ay==by): 
            if(by not in range(min(ay,cy),max(ay,cy)+1)): turn=2
            turn+=0
        else: turn+=1
    else: turn+=2
    print("YES") if(turn<2) else print("NO")