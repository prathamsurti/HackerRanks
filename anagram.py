def counter(iterable): 
    '''
    Counts the number of times an element has occured in an iterable 
    Params: 
        Iterable : A collection of hashable elements (e.g. list , tuples , strings etc. )


    Output : 
        dict : A dictionary where the key is the element in the iterable and value is it's number of occurrences 

    
    Example : 
        sample = [1,32,43,12,3,2,1]
        print(counter(sample))

        {1:2 , 32 : 1 , 43:1 , 12 : 1 , 3: 1 , 2 : 1 }
    '''
    counted = {}
    for i in iterable: 
        if i in counted: 
            counted[i] += 1
        else:
            counted[i] = 1 
    return counted

def lower(s):

    '''
    Converts the uppercase string into lowercase and ignores lower case letter or any special characters 


    input  : 
        string : A string which might or might not contain uppercase letter 
    
    output : 
        string : It returns a string that has it's all characters in lowercase 
    
    
    example : 
        print(lower('Pratham'))

        pratham 
    '''
    lower_case = ''
    for char in s:
        
        if 'A' <= char <= 'Z':
            lower_case += chr(ord(char) + 32)
        else:
            lower_case += char
    return lower_case

def check_anagram(source :str, target :str ): 
    '''
    Checks whether two strings are anagram or not  

    parameters : 
        source(str) : The first string to compare 
        target(str) : The second string to compare 

    Returns : 
        bool : True if both strings are anagrams else False 
    
    Example : 
        print(check_anagram('cat' , 'atc'))
        False 

    '''

    src , tgt = counter(lower(source)) , counter(lower(target)) # 

    if src.items() == tgt.items(): 
        return True 
    return False 


print(check_anagram("Pratham","mprahta"))