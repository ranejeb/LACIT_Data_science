import math
import os
import random
import sys

startspisok1=[str(i) for i in input('Новое слово  черезпробел ').split()]
slowo=random.choice(startspisok)
bukv=list(slowo)
kolbukv=len(bukv)
   


def poisk(bukvavariant,slowo):
    if any( bukvavariant in slowo for bukvavariant in slowo ):
        print(bukvavariant)
    else:
        print("you loose")

def viselniza(i):
    print("Ошибка")
    if i == 1:
        print('''|
|
|
|
| ''')
    elif i == 2:       
        print('''_______
|
|
|
|
| ''', end = "")
    elif i == 3:
        print('''_______
|/
|
|
|
| ''')
    elif i == 4:
        print('''_______
|/    |
|
|
|
| ''')
    elif i == 5:
        print('''_______
|/    |
|     O
|
|
| ''')
    elif i == 6:
        print('''_______
|/    |
|     O
|     |
|
| ''')
    elif i == 7:
        print('''_______
|/    |
|     O
|   //|
|
| ''')
    elif i == 8:
        print('''_______
|/    |
|     O
|   //|\\
|
| ''')
    elif i == 9:
        print('''_______
|/    |
|     O
|   //|\\
|      \\
| ''')
    elif i == 10:
        print('''_______
|/    |
|     O
|   //|\\
|   // \\
| ''')
        print("you looooose")

i = 0
while searchable != word and i < 10:
    j = 0
    f = True
    letter = input(" Введите предполагаемую букву : ")
    letter = letter.lower()
    while j < len(searchable):
        if letter == searchable[j]:
            word[j] = letter
            f = False
        elif j == len(searchable)-1 and f == False:
            break
        j+=1
    else:
        i+=1
        viselniza(i)
    print(word)
if i == 10:
    print("Проигрыш") 
else :
    print("Победа")



