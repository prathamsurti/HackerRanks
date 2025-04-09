from collections import Counter 

def check_anagram(target :str, source :str): 
    count = 0
    
    c,j = Counter(target.lower()) , Counter(source.lower())

    if c.items() <= j.items(): 
        return True 
    else :
        return False 


print(check_anagram("ratham" , "rathamPP")  )

