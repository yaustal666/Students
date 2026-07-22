#next attempt
a = int(input())
nums = [i for i in range(1, a + 1)]
count = 0
result = []
def divisibility(a: int, nums: int, count: int):
    for i in range(len(nums)):
        if a % nums[i] == 0:
            result.append('True')
            count += 1
        else:
            result.append('False')
    print(count)
divisibility(a, nums, count)
# print(result) # worked out but as i said:only in cunning way not in actual way u assumed me to do

# Опять же - список не нужен nums, переменные result и count надо засунуть в функцию
# функция должна возвращать число, в 6 задании предлагается не испольовать список results чтобы сделать то же самое
