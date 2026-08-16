#Pyramid
p = int(input('enter number'))
n = "_"
l = "x"
for i in range(0, p):
    print(n[i - 1: :-1], n[i : ], end = '')
    for m in range(i, p):
        print(l[i + 1: ], l[i:], end = '') 