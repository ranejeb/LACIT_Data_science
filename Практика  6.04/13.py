spisok = [1, 3, 4, 5 ,7, 9]
a = int(input("Ввод, "))
i = 0
number = 0
for i in range(0, len(spisok)):
    if spisok[i] == a:
        number = i + 1
        print("Элемент ",number)
        break
    i+=1
else:   
    print("Нет такого элемента ")
