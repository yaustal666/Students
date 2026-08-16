a = int(input())
nums = [i for i in range(1, a + 1)]
result = []
def divisibility(a: int, nums: int):
    for i in range(len(nums)):
        if a % nums[i] == 0:
            result.append('True')
        else:
            result.append('False')
divisibility(a,nums)
print(result) # ok

# Тебе не нужен список nums, ты можешь запустить цикл от 2 до a вместо того чтобы идти по списку
# И сделай пожалуйста так, чтобы функция возвращала список, а не модифицировала внешний