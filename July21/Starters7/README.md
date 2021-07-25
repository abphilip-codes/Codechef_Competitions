# July 2021: Starters 7

```
1. Given the time control of a chess match as a+b, determine which format of chess out 
of the given 4 it belongs to.
    1) Bullet if a+b<3
    2) Blitz if 3≤a+b≤10
    3) Rapid if 11≤a+b≤60
    4) Classical if 60<a+b

Input Format

    First line will contain T, number of testcases. Then the testcases follow.
    Each testcase contains a single line of input, two integers a,b.

Output Format

    For each testcase, output in a single line, answer 1 for bullet, 2 for blitz, 
    3 for rapid, and 4 for classical format.

Constraints

    1≤T≤1100
    1≤a≤100
    0≤b≤10

Sample Input 1

    4
    1 0
    4 1
    100 0
    20 5

Sample Output 1

    1
    2
    4
    3

Explanation

    TestCase 1: Since a+b=1<3, it belongs to bullet format.
    TestCase 2: Since 3≤(a+b=5)≤10, it belongs to blitz format.
```
<br />

```
2. A great deal of energy is lost as metabolic heat when the organisms from one trophic 
level are consumed by the next level. Suppose in Chefland the energy reduces by a factor 
of K, i.e, if initially, the energy is X, then the transfer of energy to the next tropic 
level is ⌊X/K⌋. This limits the length of foodchain which is defined to be the highest 
level receiving non-zero energy. E is the energy at the lowest tropic level. Given E and 
K for an ecosystem, find the maximum length of foodchain. Note: ⌊x⌋ denoted the floor 
function, and it returns the greatest integer that is less than or equal to x (i.e rounds 
down to the nearest integer). For example, ⌊1.4⌋=1, ⌊5⌋=5, ⌊−1.5⌋=−2, ⌊−3⌋=−3, ⌊0⌋=0.

Input Format

    First line will contain T, number of testcases. Then the testcases follow.
    Each testcase contains a single line of input, two integers E,K.

Output Format

    For each testcase, output in a single line answer to the problem.

Constraints

    1≤T≤10^4
    1≤E≤10^9
    2≤K≤10^9

Sample Input 1

    3
    5 3
    6 7
    10 2

Sample Output 1

    2
    1
    4

Explanation

TestCase 1: The energy at first level is 5 units. For the second level energy becomes 
⌊53⌋=1 units. So the length of foodchain is 2 since from the next level onwards 0 units
of energy will be received.

TestCase 3: The energy at different levels is:
    Level 1 - 10 units
    Level 2 - ⌊10/2⌋ = 5 units
    Level 3 - ⌊5/2⌋ = 2 units
    Level 4 - ⌊2/2⌋ = 1 units
    Level 5 - ⌊1/2⌋ = 0 units

So the answer is 4, since it is the last level to receive non-zero energy.
```
<br />

```
3. During a fight with the Joker, Batman's eyes lose the capability to distinguish 
between some pairs of colors. Each color has an integer ID from 1 to N. There are 
M lists where each color belongs to exactly one list. Batman can distinguish colors belonging to different lists, but he cannot distinguish colors belonging to the same 
list. Given a strip of L colors, find the different number of segments Batman will 
see as a result of his disability. Two positions of the strip are said to belong to 
the same segment if they are adjacent on the strip and Batman cannot distinguish their 
colors. See the sample explanation for clarity.

Input Format

    The first line contains an integer T, the number of test cases. 
    Then the test cases follow.
    The first line contain three integers N, M, and L - the number of colors, the 
    number of lists, and the length of the strip, respectively.
    Each of the next M lines describes a list. It begins with an integer Ki, 
    the length of the i-th list, followed by Ki integers Ai1,Ai2,…,AiKi - the color 
    IDs of the i-th list.
    The next line contains L integers S1,S2,…,SL - the color IDs of the strip.

Output Format

    For each test case, output in a single line the answer to the problem.

Constraints

    1≤T≤10
    1≤M≤N≤10^5
    1≤L≤10^5
    1≤Ki,Aij,Si≤N
    ∑Mi=1Ki=N

    Each color belongs to exactly one list.

Sample Input 1

    3
    2 2 2
    1 2
    1 1
    2 1
    2 2 4
    1 1
    1 2
    1 2 2 1
    3 2 3
    2 1 3
    1 2
    1 3 1

Sample Output 1

    2
    3
    1

Explanation

    Test Case 1: Since the strip is composed of colors from different lists, the 
    answer is the length of the strip, which is 2.
    Test Case 2: The first and second index have colors from different lists, and the 
    third and fourth index have colors from different lists. So the strip is seen to 
    be composed of 3 consecutive segments.
    Test Case 3: Since the strip is composed of colors from the same list, the answer 
    is 1 segment.
```
<br />

```
4. You are given an array A consisting of N integers and Q queries. Each query is 
described by two integers L and R. For each query, output the number of tuples (i,j,k) 
such that L≤i<j<k≤R and Ai+Aj+Ak is an even number.

Input Format

    The first line contains an integer T, the number of test cases. Then the test cases 
    follow. The first line of each test case contains two integers N and Q. The next line 
    contains N integers A1,…,AN. Then Q lines follow, each containing two integers Li 
    and Ri.

Output Format

    For each query, output the number of tuples possible as mentioned in the 
    problem statement.

Constraints

    1≤T≤10^3
    1≤N,Q≤10^5
    0≤Ai≤10^6
    1≤Li≤Ri≤N

    The sum of N over all test cases does not exceed 10^6.
    The sum of Q over all test cases does not exceed 10^5

Sample Input 1

    1
    6 3
    1 2 3 4 5 6
    1 3
    2 5
    1 6

Sample Output 1

    1
    2
    10

Explanation

    For the first query, we can choose (1,2,3) since A1+A2+A3=6 is an even number. 
    For the second query, we can choose (2,3,5) since A2+A3+A5=10 is even, and (3,4,5) 
    since A3+A4+A5=12 is even.
```