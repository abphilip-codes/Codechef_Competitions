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
3. Value of an array A of length L is defined as the sum of (Ai⊕i) for all 0≤i<L, where ⊕
denotes bitwise xor operation. Note that array indices start from zero. You are given an integer N and an array A consisting of 2^N integers where Ai=i for all 0≤i<2^N.

Example :

    For N=1, you have an array A of length 21=2 and A=[0,1].
    For N=2, you have an array A of length 22=4 and A=[0,1,2,3].

    You can do at most K operations on this array. In one operation, you can choose two 
    indices i and j (0≤i,j<2N) and swap Ai and Aj (i.e. Ai becomes Aj and vice versa).
    What is the maximum value of array A you can obtain after at most K operations?

Input Format

    First line will contain T, number of testcases. Then the testcases follow.
    Each testcase contains a single line of input, two integers N,K.

Output Format

    For each testcase, output in a single line the maximum value of array after 
    doing at most K operations.

Constraints

    1≤T≤10^5
    1≤N≤30  
    0≤K≤10^9

Sample Input 1

    3
    2 0
    2 1
    10 100

Sample Output 1

    0
    6
    204600

Explanation

    In the first test case, for N=2, you have the array A=[0,1,2,3]. No swap operation 
    is allowed hence value of array A=(0⊕0)+(1⊕1)+(2⊕2)+(3⊕3)=0+0+0+0=0.
    
    In the second test case, initially the array A=[0,1,2,3]. If you swap A1 and A2, 
    A becomes [0,2,1,3]. Now value of array A=(0⊕0)+(2⊕1)+(1⊕2)+(3⊕3)=0+3+3+0=6. There 
    is no possible way such that value of array A becomes greater than 6 using one swap operation.
```
<br />

```
4. You are given two integers A,B. You have to choose an integer X in the range 
[minimum(A,B), maximum(A,B)] such that: ⌈(B−X)/2⌉+⌈(X−A)/2⌉ is maximum. What is the 
maximum sum you can obtain if you choose X optimally?

Note: ⌈x⌉ Returns the smallest integer that is greater than or equal to x (i.e rounds up 
to the nearest integer). For example, ⌈1.4⌉=2, ⌈5⌉=5, ⌈−1.5⌉=−1, ⌈−3⌉=−3, ⌈0⌉=0.

Input Format

    First line will contain T, number of testcases. Then the testcases follow.
    Each testcase contains of a single line of input, two integers A,B.

Output Format

    For each testcase, output the maximum sum of ⌈(B−X)/2⌉+⌈(X−A)/2⌉.

Constraints

    1≤T≤10^5
    1≤A,B≤10^9

Sample Input 1

    3
    2 2
    1 11
    13 6

Sample Output 1

    0
    6
    -3

Explanation

    In the first test case, there is only one possible value of X which is equal to 2. 
    So the sum is equal to ⌈(2−2)/2⌉+⌈(2−2)/2⌉ = ⌈0⌉+⌈0⌉ = 0+0=0.

    In the second test case, we can choose X to be 2. So sum is equal to ⌈(11−2)/2⌉+
    ⌈(2−1)/2⌉ = ⌈ 4.5⌉+⌈ 0.5⌉ = 5+1=6. There is no possible way to choose an integer X 
    in the range [1,11] such that sum is greater than 6.
```