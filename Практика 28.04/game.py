4

import random

number_true=random.randint(0,10)

def gamerandom(number):
    #number_true=random.randint(0,10)
    print(number_true)

    answer = (True if number==number_true else False )
    #print("Победа" if answer==True else "Попробуйте еще раз")
    return answer

def vvod(number):
    if gamerandom(number)==False:
        print(" Попробуйте еще раз ")
        n=int(input(" Введите число "))
        gamerandom(n)
    else:
        print("Победа")
    return 

    """
    if gamerandom(number) == False:
        print(" Попробуйте еще раз ")
        n=int(input(" Введите число "))
    else:
        print(" Победа ")
"""

 
print(vvod(3))

