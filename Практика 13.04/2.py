def f(a,b):
    if a > b:
        print ("1 число больше")
    elif a < b:
        print("2 число больше")
    elif a == b:
        print("числа равны")
x = float(input("Введите число: "))
y = float(input("Введите число: "))
f(x,y)