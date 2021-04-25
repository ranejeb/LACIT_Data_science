def f1(n):
    for x in range (0,n):
        for y in range (x+1, n):
            yield(x,y)        
n = int(input("Введите число, "))
