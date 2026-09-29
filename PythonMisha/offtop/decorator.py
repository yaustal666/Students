def decor(foo):

    def wrap():
        print("before")
        foo()
        print("after")

    return wrap

@decor
def f():
    print("Hello world")