someList = input().split()
a = input()

# print(someList)
# print(type(a))

# if a in someList:
#     print(someList.index(a))
# else:
#     print(None)

# def lenN(a: list) -> int:
#     count = 0
#     for i in a:
#         count += 1
#     return count

# a = lenN([1, 2, 3, 4])
# print(a)


flag = True
for i in range(len(someList)):
    if someList[i] == a:
        print(i)
        flag = False
if flag == True:
    print(None)

# def indexX(a, b) -> int:
#     for i in range(len(a)):
#         if a[i] == b:
#             return i
#     return None

# print(indexX(someList, a))