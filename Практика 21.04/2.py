num=int(input(' Введите число - '))
def prim(n):
    for x in range(1, n+1):
        if n % x == 0:
            yield x
            
print(next(prim(num)))
print(next(prim(num)))
print(next(prim(num)))
print(next(prim(num)))