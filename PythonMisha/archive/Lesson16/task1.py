class A:
    def __init__(self, num: int):
        self.number = num

class B:
    def __init__(self, a: A, amount: int):
        self.a = a
        self.amount = amount

class C:
    def __init__(self, b: list[B]):
        self.b_list = b

a1 = A(10)
print('a1: ', a1)
print(a1.number)

b1 = B(a1, 125)
print('b1: ', b1)
print('b1.a: ', b1.a)
print('b1.a.number: ', b1.a.number)

c = C([b1])
print(c)
print(c.b_list)
print(c.b_list[0])
print(c.b_list[0].a)
print(c.b_list[0].a.number)