""""
#Задание 1
a = int(input("Введите a = "))
b = int(input("Ведите b = "))
if a > b:
  print ("a больше")
elif a < b:
  print ("b больше")
else :
  print ("они равны")

#Задание 2
a = float(input("Введите a = "))
b = float(input("Ведите b = "))
if a > b:
  print ("a больше")
elif a < b:
  print ("b больше")
else :
  print ("они равны")

#Задание 3

stroka=input()

def razb(stroka):
  return[char for char in stroka]
 
def probel(stroka1):
  for element in razb(stroka):
    if element in razb(stroka)  :

#Задание 4
from itertools import chain

def up_and_down(n):  # 1,2, ..., n, ..., 2, 1
    return chain(range(1, n), range(n, 0, -1))

def diamond(n):
    for i in up_and_down(n):
        print((n-i)*' ', *up_and_down(i), sep='') 
        


print(diamond(3))

#Задание 8
classr=(input("Введите класс  "))
B="perv" if classr in "1234" else "wtoraya" if classr in "456789" else "tretia"
print(B)


#Задание 9
stoka=input()
def enum(stoka):
  for char in stoka:
    print(ord(char))

print(enum(stoka))

#Задание 10
stoka=input()
i=0
s=0
def enum(stoka,i,s):
  for char in stoka[i]:
    s=s+ord(stoka[i])
    i=+1
    return s

print(enum(stoka,i,s))
"""
List1 = []  # заводим пустой список
n = int(input())  # считываем количество элемент в списке
for i in range(n):  
    new_element = int(input())  # считываем очередной элемент
    List1.append(new_element)  # добавляем его в список
    # последние две строки можно было заменить одной:
    # a.append(int(input()))
print(List1)
list2=(List1.sort())
c="1" # символ 't'
i=0
while i<5:
    j=0
    k=0
    while j<len(list2[i]):
        if c==List1[i][j]:
            k=k+1
            print("я тут")
            j=j+1
    i=i+1
