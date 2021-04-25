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
