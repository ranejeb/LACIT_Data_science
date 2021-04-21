def range_generator(a, *x):
    print('range generator start', a, x)
    if len(x)>2:
        raise TypeError("Too many arguments")
    i=a if x else 0
    n=x[0] if len(x)>0 else a
    s=x[1] if len(x)>1 else 1
    t = (lambda *k: k)(a,*x)
    while i<n : t= yield i; i+=s
    print('range generator stop', a, x)
    if type(t) is int: t=t,
    if type(t) is not tuple:t = (lambda *k: k)(a,*x)
    return t
def expander (*a):
    print('expander start', a)
    try:
        while True:
            a=(yield from range_generator(*a))
            print('expander next', a)
    finally:
        print('expander stop',a)

g=expander(3)
print(next(g))
print(next(g))
print(next(g))
print(g.send(2))