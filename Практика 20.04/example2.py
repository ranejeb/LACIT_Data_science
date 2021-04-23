def g(n):
    yield from (x**2 for x in range(n))

for x in g(4):print(x)