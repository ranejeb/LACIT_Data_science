n = int(input("Введите число, "))

def gen_for_exercise5(n):
    for i in (str(i)+" "+str(j) for i in range(n) for j in range(i, n) if i < j):
        for j in i:
            if j in ['0','1','2','3','4','5','6','7','8','9']:
                yield j
for i in gen_for_exercise5(n):
    print(i)