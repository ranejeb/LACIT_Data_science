# задание 1
'''
n=int(input(' Введите число - '))

a=[(i,j) for i in range(0,n-1) for j in range(0,n-1) if j > i]
print(a)
'''
#задание 2
num=int(input(' Введите число - '))
count=0
def prim(n,count):
    for i in n:
        while count != 0 :
            if n % i == 0:
            yield i
            i+=1
            count+=1
print(prim(num))
  
          
'''
a=[i for i in range(1,n+1) if n % i == 0]
print(a)
'''

#Задание 3
'''
n=int(input(' Введите число - '))

a=[(i,j) for i in range(0,n-1) for j in range(0,n-1) if j > i] # задание 1
b=[i for i in range(1,n+1) if n % i == 0] # задание 2

c=[i for i in a[0:2:]+b[2::]]

print (c)
'''
#Задание 4
'''
n=int(input(' Введите число - '))

a=[(i,j) for i in range(0,n-1) for j in range(0,n-1) if j > i] # задание 1

c=[i for i in a]

print(c)
'''
#Задание 5

#Задание 6

#Задание 7
'''
import asyncio

def read_file(file_name):
    return open(file_name, 'r')

async def main():
    loop = asyncio.get_event_loop()
    d= await loop.run_in_executor(None, read_file, 'text.txt')
    print(d)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
'''