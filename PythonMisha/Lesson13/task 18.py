"""
Question: A website requires the users to input username and password to register.
Write a program to check the validity of password input by users. Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1

"""

def webRegistration(a : str) -> list:
    valid =[]
    traits = {
    'has_min' : False,  
    'has_max' : False,
    'has_letter' : False,
    'has_character' : False,
    'has_num' : False,
    'has_upper' :False,
    'has_lower' : False
    } #default mutable traits
    
    if len(a) >= 6 and len(a) <= 12:
        traits['has_min'] = True
        traits['has_max'] = True
        for char in a:
            if char in 'abcdefghijklmnopqrstuvwxyz': # mistake in  indentations(all if's nested)
                traits['has_letter'] = True   #had char after equal sign instead of True thinking that i would have got True by assigning char
            if char in '@#$':
                traits['has_character'] = True
            if char in '1234567890':
                traits['has_num'] = True
            if char.isupper() == True: # came to this logic on myself only after 25 sec
                traits['has_upper'] = True
            if char.islower() == True:
                traits['has_lower'] = True
        check = [i for i in traits.values()]
        s = [ i if i == True else False for i in check ]
        n = [valid.append(a) if all(s) == True else 0] 
    return print(valid)
        
        
    
    
for i in  input().split(','):  #made my me and ai just fixed absentism of ','
    s = webRegistration(i)