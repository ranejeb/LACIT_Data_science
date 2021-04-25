# задание 1

n=int(input(' Введите число - '))

a=((i,j) for i in range(0,n-1) for j in range(0,n-1) if j > i)

print(next(a))
print(next(a))
print(next(a))
print(next(a))