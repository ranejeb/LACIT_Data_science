def fn(a):
    spisok = [1, 3, 4, 5 ,7, 9]
    i = 0
    number = 0
    while(i < len(spisok)):
        if spisok[i] == a:
            number = i + 1
            print("Элемент ",number)
            break
        i+=1
    else:   
        print("Нет такого ")
fn(int(input("введите число , ")))