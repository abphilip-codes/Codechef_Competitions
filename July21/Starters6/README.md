# July 2021: Starters 6

```
1. In a season, each player has three statistics: runs, wickets, and catches. Given 
the season stats of two players A and B, denoted by R, W, and C respectively, the 
person who is better than the other in the most statistics is regarded as the better
overall player. Tell who is better amongst A and B. It is known that in each statistic, 
the players have different values.

Input Format

    The first line contains an integer T, the number of test cases. Then the test 
    cases follow. Each test case contains two lines of input. The first line contains 
    three integers R1, W1, C1, the stats for player A.
    The second line contains three integers R2, W2, C2, the stats for player B.

Output Format

    For each test case, output in a single line "A" (without quotes) if player A
    is better than player B and "B" (without quotes) otherwise.

Constraints

    1≤T≤1000
    0≤R1,R2≤500
    0≤W1,W2≤20
    0≤C1,C2≤20
    R1≠R2
    W1≠W2
    C1≠C2

Sample Input 1

    3
    0 1 2
    2 3 4
    10 10 10
    8 8 8
    10 0 10
    0 10 0

Sample Output 1

    B
    A
    A

Explanation

    Test Case 1: Player B is better than A in all 3 fields.
    Test Case 2: Player A is better than B in all 3 fields.
    Test Case 3: Player A is better than B in runs scored and number of catches.
```
<br />

```
2. There are three people, and each of them has an unbiased 6-sided die. The result 
of rolling a die will be a number between 1 and 6 (inclusive) with equal probability.
The three people throw their dice simultaneously. In this game, the third person wins 
only if his number is strictly greater than the sum of the other two numbers. Given 
that the first person rolls the value X and the second person rolls the value Y, what 
is the probability the third person will win?

Input Format

    The first line contains an integer T, the number of test cases. Then the test 
    cases follow. Each test case contains two integers X and Y.

Output Format

    For each test case, output the probability that the third person wins.
    Your answer will be considered correct if its absolute error doesn't exceed 10−6.

Constraints

    1≤T≤36
    1≤X,Y≤6

Sample Input 1

    3
    1 3
    2 4
    2 3

Sample Output 1

    0.333333
    0
    0.166666

Explanation

    In the first test case, out of the six outcomes of a die, the third person wins 
    if the result is either 5 or 6. So the probability of winning is 26≈0.333333.
    In the second test case, the third person only wins if the result is greater than 
    6, which is impossible. So the probability of winning is 0.
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
4. You are the owner of a big company. You are so rich, that the government 
has allowed you to print as many notes as you want of any single value that 
you like. You also have peculiar behavioral traits and you often do things 
that look weird to a third person.

You have N employees, where the i-th employee has salary Ai. You want to pay 
them using a denomination that you create. You are also eco-friendly and wish 
to save paper. So, you wish to pay them using as few notes as possible. Find 
out the minimum number of notes required if you can alter the salary of at most 
one employee to any positive integer that you like, and choose the positive 
integer value that each note is worth (called its denomination).

Each employee must receive the exact value of his/her salary and no more.

Input

    The first line contains an integer T, the number of test cases. 
    Then the test cases follow.
    
    The first line of each test case contains a single integer N
    The second line contains N integers A1,A2,…,AN, where Ai is 
    the salary of the i-th employee.

Output

    For each test case, output in a single line the answer to the problem.

Constraints

    1≤T≤12⋅10^4
    1≤N≤10^5
    1≤Ai≤10^9
    The sum of N over all test cases is at most 10^6

Subtasks

    Subtask #1 (100 points): Original constraints

Sample Input

    3
    3
    1 2 3
    3
    8 4 2
    2
    2 2 

Sample Output

    4
    4
    2

Explanation

    Test Case 1: We can change the salary of the third person to 1 and use 
    1 as the denomination. So in total we need 1/1+2/1+1/1 = 1+2+1 = 4 notes.

    Test Case 2: We can change the salary of the first person to 2 and use 
    2 as the denomination. So in total we need 1+2+1 = 4 notes.

    Test Case 3: We can use 2 as the denomination and we need not change 
    the salary of any person. So in total we need 1+1 = 2 notes.
```