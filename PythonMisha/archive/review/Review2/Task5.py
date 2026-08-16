a = int(input())
nums = [i for i in range(1, a + 1)]
count = 0
result = []
question = input('which operation? ')
def divisibility(a: int, nums: int, count: int):
    if question == 'divisors':
        for i in range(len(nums)):
            if a % nums[i] == 0:
                result.append('True')
                count += 1
            else:
                result.append('False')
    else:
        if a % 2 == 0 or a % 3 == 0:
            return 'composite'
        else:
            return 'prime'
print(divisibility(a,nums,count)) 
#got stuck a bit with second else to adgust logic but not 
# abstruse stuff but what really took some brainstome is 'none' output that i fixed 

# То то же что и в предыдущих, переменные внутрь функции, возвращает только True False - является ли число простым
# В предудущем задании ты получил результат - количество делителей
# если их 2 - то есть единица и само число, то число простое, question не нужен здесь