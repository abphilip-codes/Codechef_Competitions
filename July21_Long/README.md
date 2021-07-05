# July 2021: Long Challenge

```
1. Chefland has 7 days in a week. Chef is very conscious 
about his work done during the week. There are two ways he 
can spend his energy during the week. The first way is to do x
units of work every day and the second way is to do y (>x) 
units of work for the first d (<7) days and to do z (<x) units 
of work thereafter since he will get tired of working more in 
the initial few days.

Find the maximum amount of work he can do during the week if 
he is free to choose either of the two strategies.

Input

    The first line contains an integer T, the number of test cases. 
    Then the test cases follow.
    Each test case contains a single line of input, four integers 
    d, x, y, z

Output

    For each testcase, output in a single line the answer to the problem.

Constraints

    1≤T≤5*10^3
    1≤d<7
    1≤z<x<y≤18

Subtasks

    Subtask #1 (100 points): Original constraints

Sample Input

    3
    1 2 3 1
    6 2 3 1
    1 2 8 1

Sample Output

    14
    19
    14

Explanation

    Test Case 1: Using the first strategy, Chef does 2⋅7=14 units of 
    work and using the second strategy Chef does 3⋅1+1⋅6=9 units of work. 
    So the maximum amount of work that Chef can do is max(14,9)=14 
    units by using the first strategy.

    Test Case 2: Using the first strategy, Chef does 2⋅7=14 units of work 
    and using the second strategy Chef does 3⋅6+1⋅1=19 units of work. So the 
    maximum amount of work that Chef can do is max(14,19)=19 units by using 
    the second strategy.
```
<br />

```
2. n Chefland, the speed of light is c m/s, and acceleration due to gravity is 
g m/s^2. Find the smallest height (in meters) from which Chef should jump such 
that during his journey down only under the effect of gravity and independent of 
any air resistance, he achieves the speed of light and verifies Einstein's theory 
of special relativity.

Assume he jumps at zero velocity and at any time, his velocity (v) and depth of 
descent (H) are related as v^2=2⋅g⋅H.

Input

    The first line contains an integer T, the number of test cases. Then the 
    test cases follow.
    Each test case contains a single line of input, two integers g, c

Output

    For each test case, output in a single line the answer to the problem. We can 
    show that under the constraints, the answer is an integer.

Constraints

    1≤T≤5*10^3
    1≤g≤10
    1000≤c≤3000
    2⋅g divides c^2

Subtasks

    Subtask #1 (100 points): Original constraints

Sample Input

    3
    7 1400
    5 1000
    10 1000

Sample Output

    140000
    100000
    50000

Explanation

    Test Case 1: For Chef to achieve the speed of light, the minimum height 
    required is c^2/2⋅g = 1400⋅1400/14 = 140000 meters.

    Test Case 3: For Chef to achieve the speed of light, the minimum height 
    required is c^2/2⋅g = 1000⋅1000/20 = 50000 meters.
```
<br />

```
3. Given an array A1,A2…AN, find the minimum number of operations (possibly zero)
required to convert all integers in A to 0

In one operation, you choose a non-negative integer p (p≥0), select at most K 
indices in the array A, and for each selected index i, replace Ai with Ai⊕2^p. 
Here, ⊕ denotes bitwise XOR.

Input

    The first line contains an integer T - the number of test cases. 
    Then T test cases follow.
    The first line of each test case contains two integers N, K - the 
    size of the array and the maximum number of elements you can select 
    in an operation.
    The second line of each test case contains N integers A1,A2…AN

Output

    For each test case, output the minimum number of operations to make all 
    elements of the array 0

Constraints

    1≤T≤10^5
    1≤N,K≤10^5
    0≤Ai≤10^9
    The sum of N over all test cases does not exceed 2*10^5

Subtasks

    Subtask #1 (100 points): Original Constraints

Sample Input

    1
    3 2
    3 6 10

Sample Output

    5

Explanation

    Here is one way to achieve [0,0,0]
    from [3,6,10] in 5

Operations:

    Choose p=0 and indices {1}. Now A becomes [2,6,10].
    Choose p=1 and indices {1,2}. Now A becomes [0,4,10]
    Choose p=1 and indices {3}. Now A becomes [0,4,8]
    Choose p=2 and indices {2}. Now A becomes [0,0,8]
    Choose p=3 and indices {3}. Now A becomes [0,0,0]

    It can be shown that at least 5 operations are required.
```
<br />

```
4. 
```