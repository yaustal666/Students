def foo(n, m, *args, **kwargs):
    print(n)
    print(m)
    print(args)
    print(kwargs)

a = [1, 2, 3]
n, m, k = a