n = input()

# a = n
# s = 0
# for i in range(4):
#     s += a
#     a = a * 10 + n

# print(s)

a = n
s = 0
for i in range(4):
    s += int(a)
    a = a + n
print(s)

# s = 0
# a = "5"
# n = "5"

# s += int(a)
# print(type(s), s)
# print(type(a) , a)

# a = a + n
# s += int(a)
# print(type(s), s)
# print(type(a) , a)