n = list(map(int, input().split(',')))
# n = [int(x) for x in input().split()]

from math import sqrt, floor, trunc, ceil

def root(d : list):
    c = 50 
    h = 30
    for i in d:
        q = c * i * 2 / h
        print(round(sqrt(q)))

root(n)