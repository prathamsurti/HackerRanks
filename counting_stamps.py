'''
Problem Statement:
-------------------
You are given `N` country names, one per line.

Your task is to:
1. Read all `N` country names.
2. Count how many **unique** countries are present (case-sensitive).
3. Print the count of unique countries.

Example:
Input:
4
India
USA
India
Canada

Output:
3
'''

countries = set()
N = int(input())

for i in range(N): 
    countries.add(input())
    
print(len(countries))




countries = set()
N = int(input())

for i in range(N): 
    countries.add(input())
    
print(len(countries))
