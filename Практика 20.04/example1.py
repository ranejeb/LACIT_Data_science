def g1():
    yield 1
    yield 2
def g2():
    g = g1()
    try:
        yield next(g)
        yield next(g)
        yield next(g)
    except StopIteration:
        pass