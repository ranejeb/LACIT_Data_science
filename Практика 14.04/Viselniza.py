import math
import os
import random
import sys

startspisok=[str(i) for i in input('Новое слово  черезпробел ').split()]
slowo=random.choice(startspisok)
search=list(slowo)
search=[x for x in search]
search1=[" __ " for x in search]
   
count=0


def viselniza(count):
    print("Ошибка")
    if count == 1:
        print('''|
|
|
|
| ''')
    elif count == 2:       
        print('''_______
|
|
|
|
| ''', end = "")
    elif count == 3:
        print('''_______
|/
|
|
|
| ''')
    elif count == 4:
        print('''_______
|/    |
|
|
|
| ''')
    elif count == 5:
        print('''_______
|/    |
|     O
|
|
| ''')
    elif count == 6:
        print('''_______
|/    |
|     O
|     |
|
| ''')
    elif count == 7:
        print('''_______
|/    |
|     O
|   //|
|
| ''')
    elif count == 8:
        print('''_______
|/    |
|     O
|   //|\\
|
| ''')
    elif count == 9:
        print('''_______
|/    |
|     O
|   //|\\
|      \\
| ''')
    elif count == 10:
        print('''_______
|/    |
|     O
|   //|\\
|   // \\
| ''')
        print("you looooose")


while search != search1 and count < 10:
    count1 = 0
    f = True
    bukv = input(" Введите предполагаемую букву : ")
    bukv = bukv.lower()
    while count1 < len(search):
        if bukv == search[count1]:
            search1[count1] = bukv
            f = False
        elif count1 == len(search)-1 and f == False:
            break
        count1+=1
    else:
        count+=1
        viselniza(count)
    print(search1)
if count == 10:
    print("you loose") 
else :
    print("congratulation")



