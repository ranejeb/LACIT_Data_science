
#1
print("Hello World")
#2
stroka="hello"
print (stroka)
#4
print(len(stroka))
#5
print(stroka[2])
#6
spisok=list('kors')
print(spisok)
#7
spisok2=['2',1]
print(spisok2)
#8
spisok2.append('rigald')
print(spisok2)
#9
dictionary={'ralf':'mikelson'}
print(dictionary)
#10
print(dictionary['ralf'])
#11
dictionary['туфля']='род обуви, закрывающей ногу выше щиколотки'
print(dictionary)
#12
dictionary['туфля']='хорошая туфля'
print(dictionary)
#13
del dictionary['туфля']
print(dictionary)
#14
dictionary.update({'борзая':'собака','пришелец':'марс'})
print(dictionary)
#15
znach=dictionary.get('пришелец')
print(znach)
#16
dictionary={'понедельник':36.7,'вторник':37.9,'среда':39.9,'четверг':36.8,'пятница':40.1,'суббота':35.1,'воскресение':37.3}
for value in dictionary.values():
   if value >= 37.0 :
    print(value)
   else:
    print ("Error")

    
    
    



































