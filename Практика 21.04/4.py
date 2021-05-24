n = int(input("Введите число, "))


def gen_for_exercise4(n):
    for i in (str(i)+' '+str(j) for i in range(n) for j in range(i,n) if i<j):
        yield i
for i in gen_for_exercise4(n):
    print(i)


n = int(input("Введите число, "))
