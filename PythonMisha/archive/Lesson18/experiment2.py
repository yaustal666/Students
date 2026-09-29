# Dunder / magic / special methods
# Что такое super? Если класс не наследуется от чего-либо, можно ли внутри использовать super?
# __new__
# __init__
# Что за что отвечает и откуда появляется self?
# Может ли класс А создать класс B?

class B:
    def v1(self):
        print("Class B message")

class A:
    def __new__(cls):
        return super().__new__(B)

    def v1(self):
        print("Class A message")
        

a = A()
a.v1()
