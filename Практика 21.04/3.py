n=int(input(' Введите число - '))
"""
a=((i,j) for i in range(0,n-1) for j in range(0,n-1) if j > i) # задание 1
b=(i for i in range(1,n+1) if n % i == 0) # задание 2

c=(i for i in a[0:2:]+b[2::])

print (next(c))
print (next(c))
print (next(c))
print (next(c))
"""

def gen_for_exercise2(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
def gen_for_exercise1(n):
    for i in range(n):
        for j in range(i,n):
            if i<j:
                yield [i,j]

def gen_for_exercise3(n):
    gen1=gen_for_exercise1(n)
    gen2=gen_for_exercise2(n)
    try:
        yield next(gen1)
        yield next(gen1)
        next(gen2)
        next(gen2)
    except StopIteration as e:
        print('None')
        return None
    for i in gen2:
        yield i

for i in gen_for_exercise3(n):
    print(i)