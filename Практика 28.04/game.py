import random


print(dir(random))

randnum=random.randrange(1,101,1)
searchnum=int(input('Введите чило (1-100):'))

if randnum==searchnum:
    print('Вы выйграли')
else:
    print('Попробуйте еще раз')
