#Задание 4
from itertools import chain

def up_and_down(n):  # 1,2, ..., n, ..., 2, 1
    return chain(range(1, n), range(n, 0, -1))

def diamond(n):
    for i in up_and_down(n):
        print((n-i)*' ', *up_and_down(i), sep='')

print(diamond(3))