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
    traits = {
        'has_min' : False,  
        'has_max' : False,
        'has_letter' : False,
        'has_character' : False,
        'has_num' : False,
        'has_upper' :False,
        'has_lower' : False
    }
    
    if len(a) >= 6 and len(a) <= 12:
        traits['has_min'] = True
        traits['has_max'] = True
    else:
        return False
        
    for char in a:

        if traits['has_letter'] != True:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                traits['has_letter'] = True

        if char in '@#$':
            traits['has_character'] = True

        if char in '1234567890':
            traits['has_num'] = True

        if char.isupper() == True:
            traits['has_upper'] = True

        if char.islower() == True:
            traits['has_lower'] = True

    check = [i for i in traits.values()]
    if all(check):
        return True
    return False
    
for i in input().split(','):
    s = webRegistration(i)
    print(s)