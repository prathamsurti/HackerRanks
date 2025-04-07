'''
Problem Statement:
-------------------
You are given:
- An array `arr` of `n` integers.
- A set `A` containing `m` integers representing items that increase happiness.
- A set `B` containing `m` integers representing items that decrease happiness.

Each element in the array contributes:
+1 to happiness if it exists in set A  
-1 to happiness if it exists in set B

Your task is to:
1. Calculate the total happiness score.
2. Ensure data validation: throw an error if the number of inputs for `arr`, `A`, or `B` are incorrect.
'''



n , m = map(int,input().split())
 

arr = list(map(int, input().split()))
if len(arr) !=n : 
    raise ValueError(f"Expected {n} elements in array  instead got {len(arr)}")
A = set(map(int , input().split()))


if len(A) !=m : 
    raise ValueError(f"Expected {m} elements in set  instead got {len(A)}")


B = set(map(int , input().split()))
if len(B) !=m : 
    raise ValueError(f"Expected {m} elements in array  instead got {len(B)}")

hapiness = 0 

hapiness += sum(1 if num in A else 0  for num in arr ) - sum(1 if num in B else 0 for num in arr )

print(hapiness)