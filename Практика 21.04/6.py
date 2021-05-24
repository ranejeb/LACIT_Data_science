def gen_for_exercise6(x,y):
    while True:
        send= yield [x,y]
        if send=='south':
            y+=1
        if send=='east':
            x+=1
        if send=='north':
            y-=1
        if send=='west':
            x-=1
        if send=='stop':
            break


g=gen_for_exercise6(1,1)
try:
    print(g)
    print(next(g))
    print(g.send('south'))
    print(g.send('east'))
    print(g.send('north'))
    print(g.send('west'))
    print(g.send('stop'))
except StopIteration:
    pass