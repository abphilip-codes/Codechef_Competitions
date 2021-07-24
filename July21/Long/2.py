# https://www.codechef.com/JULY21C/problems/RELATIVE

for z in range(int(input())):
    g,c = map(int,input().split(" "))
    print(int(c*c/(2*g)))