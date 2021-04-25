#Задание 3
a = str(input("Введите "))
b = a[0]
i = 1
while i <  len(a)-1:
    if a[i].isdigit() == True and a[i+1] != ")" and a[i+1] != "]" and a[i+1] != "}" and a[i+1].isdigit()!=True: 
        b += a[i]
        b+=" "
    else:
        b+=a[i]
        #a = a[ :i] + ' ' + a[i: ] ???
    i+=1
b+=a[-1]
print(b)
        