'''Problem Statement:
------------------
You're given two sets of integers:
  - A set 'A' containing 'n' integers
  - A set 'B' containing 'm' integers

Task:
-----
Find and print the intersection of these two sets.

Input Format:
-------------
Line 1: Integer n (number of elements in Set A)
Line 2: n space-separated integers (elements of Set A)
Line 3: Integer m (number of elements in Set B)
Line 4: m space-separated integers (elements of Set B)

Output Format:
--------------
A set containing the intersection of Set A and Set B

Constraints:
------------
- 0 <= n, m <= 1000
- Elements are integers (could be positive, negative, or zero)

Example Input:
5
1 2 3 4 5
4
4 5 6 7

Example Output:
{4, 5}

'''

n = int(input())

A = set(map(int,input().split()))

if len(A) !=n:
    print(f'enter {n} values ')
    
m = int(input())

B = set(map(int,input().split()))

if len(B) !=m:
    print(f'enter {m} values ')
    



inters = A.intersection(B)

print(inters)

