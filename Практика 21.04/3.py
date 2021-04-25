n=int(input(' Введите число - '))

a=((i,j) for i in range(0,n-1) for j in range(0,n-1) if j > i) # задание 1
b=(i for i in range(1,n+1) if n % i == 0) # задание 2

c=(i for i in a[0:2:]+b[2::])

print (next(c))
print (next(c))
print (next(c))
print (next(c))