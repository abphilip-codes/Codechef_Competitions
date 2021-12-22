# https://www.codechef.com/START7C/problems/CHSFORMT

for T in range(int(input())):
    a,b=map(int,input().split())
    if((a+b)<3): print(1)
    elif((a+b) in range(3,11)): print(2)
    elif((a+b) in range(11,61)): print(3)
    elif((a+b)>60): print(4)