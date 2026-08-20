# Write a function that accepts a sentence as a string, splits it into individual words, 
# and converts a word to uppercase only if its length is strictly greater than 3 characters.
# Any word with 3 or fewer characters should remain unchanged.


# def upp(a : str) -> str:  # 1 attempt 
#     s = a.split()
#     need = []
#     for i in s:
#         if len(i) > 3:
#             need.append(i.upper())
#         else:
#             need.append(i)
#     return ' '.join(need)
# print(upp('Hello world are u phyched?'))


# attempt 2 (list comprehension)


# def upp(a : str) -> str:
#     print(' '.join([i.upper() if len(i) > 3 else i for i in a.split()])) # ai explained the conception but wrote by myself
# upp('Hello world are  u excited?')


# !!!the further tasks are ai generated  to consolidate skill!!!
 #1
 
# def negReplacement(a : list) -> list:
#     print([0 if i < 0 else i for i in a]) #spent long to fix mistakes but fixed them with logic explanation from ai(not code itself)
# negReplacement([1,5,6,-1,-2])


#2

# def trasnformNum(nums : list) -> list:
#     s = [i * 2 if i % 2 == 0 else 0 for i in nums] #made mistake by usuing num * num instead of i * i
#     return s
# print(trasnformNum([1, 2, 3, 4, 5]))

#3 dict comprehansion
# def diccomp(a : list) -> dict:
#     s = {i : len(i) for i in a if len(i) > 5}
#     return s
# print(diccomp(['apple', 'banana', 'cherry']))

# 4 real practice

# def wordCounter(a: str) -> list:
#     s = {i : a.count(i) for i in a} # ai explained,wrote on myself
#     return s
# print(wordCounter(['apple', 'banana', 'apple']))


# 5 Tax caculator 

def taxCalculator(a : list) -> dict:
    taxincluded = {i : i * 1.1 for i in a if i > 10}
    return taxincluded

print(taxCalculator([15, 3, 42, 8, 20]))