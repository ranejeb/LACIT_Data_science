spisok = [1, 3, 4, 5 ,7, 9]
a = int(input("Введите , "))
i = 0
number = 0
while(i < len(spisok)):
    if spisok[i] == a:
        number = i + 1
        print("Элемент ",number)
        break
    i+=1
else:   
    print("Нет такого элемента ")