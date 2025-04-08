'''
problem statement: 
--------------------
You're given a string as an input. What u have to do is give space seperated output of  top 3 occuring letters and how many times have they occured 


input  : 
----------- 
 - String 
Output: 
----------
 top 3 most occuring letters in string with the number of ocuurences . they're sorted descending on basis of occurrence of letters  and if occurrences are same then 
 they're sorted ascending based on alphabetical order of the letters 


example usage : 
input : 'aaabbbbccdd'
output :
b 4 
a 3
c 2
d 2

'''
from collections import Counter 




s= input("Enter the String : ")

def counting(s): 
    counted = Counter(s)
    
    sorted_string = sorted(counted.items(), key = lambda item : ( - item[1] , item[0] ) )


    return sorted_string[:3]


for i in counting(s): 
    print(i[0] , i[1])